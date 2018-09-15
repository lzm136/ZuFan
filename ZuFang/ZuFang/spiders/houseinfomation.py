# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ZuFang.items import ZufangItem



class HouseinfomationSpider(CrawlSpider):
    name = 'houseinfomation'
    allowed_domains = ['dankegongyu.com']
    start_urls = ['https://www.dankegongyu.com/room/bj']

    rules = (
        # 翻页
        # https://www.dankegongyu.com/room/bj?page=4
        Rule(LinkExtractor(allow=r'room/bj\?page=\d+'), follow=True),
        # 详情页面
        # 'https://www.dankegongyu.com/room/1570683610.html'
        Rule(LinkExtractor(allow=r'room/\d+.html'), callback='parse_item',),
    )

    def parse_item(self, response):

        # city_list = response.xpath('//*[@id="topbar"]/div/div[3]/ul/li/a')
        # 获取标题列表
        house_name_list = response.xpath('//div[@class="room-detail-right"]')

        # 遍历列表，获取链接
        for node in house_name_list:
            item = ZufangItem()

            # 房屋标题
            item['house_name'] = node.xpath('./div[1]/h1/text()').extract_first()
            # 月租金
            item['monthly_rent'] = node.xpath('./div[3]/div[2]/div[1]/div/text()').extract_first()
            # 首月租金
            item['first_rent'] = node.xpath('./div[3]/div[2]/div[2]/div/text()').extract_first().strip() + '元/月'
            # 面积
            item['area'] = node.xpath('./div[4]/div[1]/div[1]/label/text()').extract_first().split(':')[-1]
            # 编号
            item['serial_number'] = node.xpath('./div[4]/div[1]/div[2]/label/text()').extract_first().split(':')[-1]
            # 户型
            item['door_model'] = node.xpath('./div[4]/div[1]/div[3]/label/text()').extract_first().strip().split(':')[-1]
            # 朝向
            item['toward'] = node.xpath('./div[4]/div[2]/div[1]/label/text()').extract_first().split(':')[-1]
            # 出租类型
            item['lease_type'] = node.xpath('./div[4]/div[1]/div[3]/label/b/text()').extract_first().split(':')[-1]
            # 楼层
            item['floor'] = node.xpath('./div[4]/div[2]/div[2]/label/text()').extract_first().split(':')[-1]
            # 区域
            item['location'] = node.xpath('./div[4]/div[2]/div[3]/label/div/a/text()').extract_first().split(':')[-1]
            # 地铁
            item['the_subway'] = node.xpath('./div[4]/div[2]/div[4]/label/text()').extract_first().split(':')[-1]

            yield item








