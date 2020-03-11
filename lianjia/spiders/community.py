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
        for each in response.xpath('//ul[@class="listContent"]/li'):
            details = CommItem()
            details['district'] = response.xpath('div[@class="positionInfo"]/a[1]/text()').extract()[0]
            details['bizcircle'] = response.xpath('div[@class="positionInfo"]/a[2]/text()').extract()[0]
            details['name'] = response.xpath('div[@class="info"]/div[@class="title"]/a/text()').extract()[0]
            try:
                details['price'] = int(response.xpath('div[@class="xiaoquListItemRight"]/div[@class="xiaoquListItemPrice"]/div[@class="totalPrice"]/span[1]/text()').extract()[0])
            except:
                details['price'] = 0
            details['sell_count'] = int(response.xpath('div[@class="xiaoquListItemRight"]/div[@class="xiaoquListItemSellCount"]/a[1]/span[1]/text()').extract()[0][:-1])

            yield details
