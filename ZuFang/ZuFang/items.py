# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZufangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 城市链接
    city_link = scrapy.Field()
    # 房屋标题
    house_name = scrapy.Field()
    # 房屋标题链接
    house_name_link = scrapy.Field()
    # 月租金
    monthly_rent = scrapy.Field()
    # 首月租金
    first_rent = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 编号
    serial_number = scrapy.Field()
    # 户型
    door_model = scrapy.Field()
    # 朝向
    toward = scrapy.Field()
    # 出租类型
    lease_type = scrapy.Field()
    # 楼层
    floor = scrapy.Field()
    # 区域
    location = scrapy.Field()
    # 地铁
    the_subway = scrapy.Field()
    pass
