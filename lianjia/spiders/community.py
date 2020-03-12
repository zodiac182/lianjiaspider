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
        for each in response.xpath('//div[@class="content"]/div[@class="leftContent"]/ul[@class="listContent"]/li[@class="clear xiaoquListItem"]'):
            details = CommItem()
            details['district'] = each.xpath('div[@class="info"]/div[@class="positionInfo"]/a[1]/text()').extract()[0]
            details['bizcircle'] = each.xpath('div[@class="info"]/div[@class="positionInfo"]/a[2]/text()').extract()[0]
            details['name'] = each.xpath('div[@class="info"]/div[@class="title"]/a[1]/text()').extract()[0]
            try:
                details['price'] = int(each.xpath('div[@class="xiaoquListItemRight"]/div[@class="xiaoquListItemPrice"]/div[@class="totalPrice"]/span[1]/text()').extract()[0])
            except:
                details['price'] = 0
            try:
             details['sell_count'] = int(each.xpath('div[@class="xiaoquListItemRight"]/div[@class="xiaoquListItemSellCount"]/a[1]/span[1]/text()').extract()[0])
            except:
                details['sell_count'] = 0

            yield details
