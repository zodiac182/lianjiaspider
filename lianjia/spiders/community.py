# -*- coding: utf-8 -*-
import scrapy
from lianjia.items import CommunityItem
import re


class CommunityspiderSpider(scrapy.Spider):
    name = 'community'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://qd.lianjia.com/xiaoqu/pg' + str(i) for i in range(1, 30)]

    def parse(self, response):
        details = CommunityItem()
        for each in response.xpath('//li[@class="clear xiaoquListItem"]'):
            details['name'] = each.xpath('div[@class="info"]/div[@class="title"]/a/text()').extract()[0]
            details['age'] = ''.join(each.xpath('div[@class="info"]/div[@class="positionInfo"]/text()').extract()).replace('\n', '').replace(' ', '')
            details['sellinfo'] = re.search(r'90.*(\d+).*', each.xpath('div[@class="info"]/div[@class="houseInfo"]/a[1]/text()').extract()[0]).group(1)
            details['position'] = ''.join(each.xpath('div[@class="info"]/div[@class="positionInfo"]/a[1]/text()').extract())
            details['position2'] = each.xpath('div[@class="info"]/div[@class="positionInfo"]/a[2]/text()').extract()[0]
            details['price'] = ''.join(each.xpath('div[@class="xiaoquListItemRight"]//div[@class="totalPrice"]//text()').extract())
            details['remark'] = each.xpath('div[@class="xiaoquListItemRight"]//div[@class="priceDesc"]/text()').extract()[0].replace(' ', '').replace('\n', '')
            details['onsell'] = ''.join(each.xpath('div[@class="xiaoquListItemRight"]//div[@class="xiaoquListItemSellCount"]/a/span/text()').extract())
            details['code'] = ''.join(each.xpath('@data-housecode').extract())
            details['count'] = (each.xpath('@data-housecode').extract())
            yield details
