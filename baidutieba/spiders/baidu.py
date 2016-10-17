# -*- coding: utf-8 -*-
import scrapy
from baidutieba.items import BaidutiebaItem
from baidutieba.items import page
import time
from scrapy.shell import inspect_response
class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = (
        'http://tieba.baidu.com/f?kw=%E8%A1%80%E5%8F%8B%E7%97%85',
    )
    

    def __init__(self, name=None, **kwargs):
        scrapy.Spider.__init__(self, name=None, **kwargs)
        self.url = 'http://tieba.baidu.com/f?kw=%E8%A1%80%E5%8F%8B%E7%97%85'
        self.page = 162300

    def parse(self, response):
        try:
            self.url = "http://tieba.baidu.com/f?kw=%D1%AA%D3%D1%B2%A1"
            for i in response.xpath('//*[@id="thread_list"]/li/div[1]/div[2]/div[1]/div[1]/a/@href'):
                href = i.extract()
                yield scrapy.Request(response.urljoin(href),callback=self.deep_parse)
            yield scrapy.Request(self.url+'&ie=utf-8&pn='+str(self.page),callback=self.parse)
            self.page += 50
            time.sleep(1)
        except KeyboardInterrupt:
            inspect_response(response,self)
    def deep_parse(self,response):
        try:
            item = BaidutiebaItem()
            item['title'] = response.xpath('//*[@id="j_core_title_wrap"]/div[2]/h1/text()')[0].extract()
            item['poster'] = response.xpath('//*[@id="j_p_postlist"]/div[1]/div[2]/ul/li[3]/a/text()')[0].extract()
            # item['post_time'] = response.xpath('')[0].extract()
            item['content'] = response.xpath('//*[contains(@id,"post_content_")]/text()')[0].extract()
            item['follower'] = response.xpath('//*[@id="thread_theme_5"]/div[1]/ul/li[2]/span[1]/text()')[0].extract()
            if not item['title']:
                inspect_response(response,self)
            return item
        except KeyboardInterrupt:
            inspect_response(response,self)