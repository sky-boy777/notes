# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BslnSpider(CrawlSpider):
    name = 'bsln'
    allowed_domains = ['baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%E5%B7%B4%E5%A1%9E%E7%BD%97%E9%82%A3']

    rules = (
        #这是帖子详情页的url
        Rule(LinkExtractor(allow=r'/p/\d+'), callback='parse_item'),
        #这是下一页的
        Rule(LinkExtractor(allow=r'https://tieba.baidu.com/f\?kw=%E5%B7%B4%E5%A1%9E%E7%BD%97%E9%82%A3&ie=utf-8&pn=\d+'), follow=True),
    )

    def parse_item(self, response):
        """处理帖子详情页"""
        item = {}
        item["标题"] = response.xpath('//div[@class="left_section"]//h3/text()').extract_first()
        item["图片"] = response.xpath('//img[@class="BDE_Image"]/@src').extract_first()
        yield item
