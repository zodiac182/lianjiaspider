import scrapy
from lianjia.items import CommItem
import time
import re


class HouseCount(scrapy.Spider):
    name = 'count'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://qd.lianjia.com/xiaoqu/1511041295482/']
    #start_urls = ['https://qd.lianjia.com/xiaoqu/pg' + str(i) for i in range(1, 2)]

    def parse(self, response):
        details = CommItem()
        details['info1'] = response.xpath('//div[@class="xiaoquDetailbreadCrumbs"]/div[@class="fl l-txt"]/a[2]/text()').extract()
        details['info2'] = response.xpath('//div[@class="xiaoquDetailbreadCrumbs"]/div[@class="fl l-txt"]/a[3]/text()').extract()
        details['info3'] = response.xpath('//div[@class="xiaoquDetailbreadCrumbs"]/div[@class="fl l-txt"]/a[4]/text()').extract()
        #details['info4'] = response.xpath('//div[@class="xiaoquDetailbreadCrumbs"]/div[@class="fl l-txt"]/a[5]/text()').extract()

        print('------'+details['info1'])
        for each in response.xpath('//div[@class="xiaoquInfo"]/div[@class="xiaoquInfoItem"]'):
            print('-------------------------------------'+each.xpath('span/text()').extract()[1])
            # if(each.xpath('div[@class="xiaoquInfoItem"]/span[@class="xiaoquInfoLabel"]/text()').extract() == "房屋总数"):
            #     details['count'] = each.xpath('div[@class="xiaoquInfoItem"]//span[@class="xiaoquInfoContent"]/text()').extract()
        print(details)
        time.sleep(3)
        yield details
        # for url in response.xpath('//ul[@class="listContent"]//li//div[@class="info"]//div[@class="title"]//a//@href'):
        #     print('------%s' %url.extract())
        #     yield scrapy.Request(url=url.extract(), callback=self.parse_detail)

    def parse_detail(self, response):
        details = CommItem()
        details['info1'] = response.xpath('//div[@class="xiaoquDetailbreadCrumbs"]/div[@class="fl l-txt"]/a[2]/text()').extract()
        details['info2'] = response.xpath('//div[@class="xiaoquDetailbreadCrumbs"]/div[@class="fl l-txt"]/a[3]/text()').extract()
        details['info3'] = response.xpath('//div[@class="xiaoquDetailbreadCrumbs"]/div[@class="fl l-txt"]/a[4]/text()').extract()
        #details['info4'] = response.xpath('//div[@class="xiaoquDetailbreadCrumbs"]/div[@class="fl l-txt"]/a[5]/text()').extract()

        print('------'+details['info1'])
        for each in response.xpath('//div[@class="xiaoquInfo"]/div[@class="xiaoquInfoItem"]'):
            print('-------------------------------------'+each.xpath('span/text()').extract()[1])
            # if(each.xpath('div[@class="xiaoquInfoItem"]/span[@class="xiaoquInfoLabel"]/text()').extract() == "房屋总数"):
            #     details['count'] = each.xpath('div[@class="xiaoquInfoItem"]//span[@class="xiaoquInfoContent"]/text()').extract()
        print(details)
        time.sleep(3)
        yield details