# -*- coding: utf-8 -*-
import scrapy
from lianjia.items import CommItem
import time


class HouseCount(scrapy.Spider):
    name = 'comm'
    allowed_domains = ['lianjia.com']
    #start_urls = ['https://qd.lianjia.com/xiaoqu/1511041295482/']
    start_urls = ['https://qd.lianjia.com/xiaoqu/pg' + str(i) for i in range(1, 31)]

    def parse(self, response):
        for url in response.xpath('//ul[@class="listContent"]//li//div[@class="info"]//div[@class="title"]//a//@href'):
            yield scrapy.Request(url=url.extract(), callback=self.parse_detail)

    def parse_detail(self, response):
        details = CommItem()
        details['info1'] = response.xpath('//div[@class="xiaoquDetailbreadCrumbs"]/div[@class="fl l-txt"]/a[2]/text()').extract()[0]
        details['info2'] = response.xpath('//div[@class="xiaoquDetailbreadCrumbs"]/div[@class="fl l-txt"]/a[3]/text()').extract()[0]
        details['info3'] = response.xpath('//div[@class="xiaoquDetailbreadCrumbs"]/div[@class="fl l-txt"]/a[4]/text()').extract()[0]
        details['name'] = response.xpath('//div[@class="xiaoquDetailbreadCrumbs"]/div[@class="fl l-txt"]/a[5]/text()').extract()[0]
        try:
            details['price'] = int(response.xpath('//div[@class="xiaoquPrice clear"]/div[@class="fl"]/span[@class="xiaoquUnitPrice"]/text()').extract()[0])
        except:
            details['price'] = 0
        details['count'] = response.xpath('//div[@class="xiaoquInfo"]/div[7]/span[2]/text()').extract()[0][:-1]

        yield details