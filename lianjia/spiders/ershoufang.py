# -*- coding: utf-8 -*-
import scrapy
from lianjia.items import LianjiaItem


class LianjiaSpider(scrapy.Spider):
    name = 'ershoufang'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://qd.lianjia.com/ershoufang/pg' + str(i) for i in range(1, 2)]  # 100页

    def parse(self, response):
        for url in response.xpath('//div[@class="info clear"]//div[@class="title"]//a//@href'):
            yield scrapy.Request(url=url.extract(), callback=self.parse_detail)

    def parse_detail(self, response):
        detail = LianjiaItem()
        detail['title'] = ''.join(response.xpath('//div[@class="title"]//h1//@title').extract())
        detail['community'] = ''.join(response.xpath('//div[@class="communityName"]//a[@class="info "]//text()').extract())
        detail['areaName'] = response.xpath('//div[@class="areaName"]//span[@class="info"]//a//text()').extract()[0]
        detail['areaName1'] = response.xpath('//div[@class="areaName"]//span[@class="info"]//a//text()').extract()[-1]
        detail['price'] = ''.join(response.xpath('//div[@class="price "]//span[@class="total"]//text()').extract()) + u'万'
        detail['unitPrice'] = ''.join(response.xpath('//div[@class="unitPrice"]//span[@class="unitPriceValue"]//text()').extract())
        detail['area'] = ''.join(response.xpath('//div[@class="area"]//div[@class="mainInfo"]//text()').extract())
        detail['forsaledate'] = ''.join(response.xpath(
            '//div[@id="introduction"]//div//div[@class="introContent"]//div[@class="transaction"]//div[@class="content"]//ul//li[1]//span[2]//text()').extract())
        detail['lastsaledate'] = ''.join(response.xpath(
            '//div[@id="introduction"]//div//div[@class="introContent"]//div[@class="transaction"]//div[@class="content"]//ul//li[3]//span[2]//text()').extract())
        detail['age'] = ''.join(response.xpath(
            '//div[@id="introduction"]//div//div[@class="introContent"]//div[@class="transaction"]//div[@class="content"]//ul//li[5]//span[2]//text()').extract())
        detail['floor'] = ''.join(response.xpath(
            '//div[@id="introduction"]//div//div[@class="introContent"]//div[@class="base"]//div[@class="content"]//ul//li[2]//text()').extract())[4:]
        detail['url'] = response.url
        detail['houserecord'] = response.xpath('//div[@class="houseRecord"]//span[@class="info"]//text()').extract()[0]
        yield detail
