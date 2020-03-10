# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # name = scrapy.Field()
    title = scrapy.Field()    # 标题
    # apartment = scrapy.Field()
    # totalarea = scrapy.Field()
    # availablearea = scrapy.Field()
    floor = scrapy.Field()    # 楼层
    # agelimit = scrapy.Field()
    forsaledate = scrapy.Field()   # 挂牌时间
    lastsaledate = scrapy.Field()  # 上次交易
    community = scrapy.Field()   # 小区名称
    area = scrapy.Field()  # 面积
    areaName = scrapy.Field()  # 所在区域
    areaName1 = scrapy.Field()  # 所在区域2
    price = scrapy.Field()  # 总价
    unitPrice = scrapy.Field()  # 单价
    age = scrapy.Field()  # 房屋年限
    url = scrapy.Field()  # url
    houserecord = scrapy.Field()  # 链家编号
    commprice = scrapy.Field()  # 小区均价


class CommunityItem(scrapy.Item):
    age = scrapy.Field()   # 小区建筑年代
    name = scrapy.Field()  # 小区名称
    sellinfo = scrapy.Field()  # 成交信息
    price = scrapy.Field()  # 均价
    onsell = scrapy.Field()  # 在售
    position = scrapy.Field()  # 位置
    position2 = scrapy.Field()  # 位置2
    remark = scrapy.Field()  # 备注
    code = scrapy.Field()  # 小区代码
    count = scrapy.Field()  # count

class CommItem(scrapy.Item):
    info1 = scrapy.Field()
    info2 = scrapy.Field()
    info3 = scrapy.Field()
    info4 = scrapy.Field()
    count = scrapy.Field()