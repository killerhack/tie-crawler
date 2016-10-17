# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

page = 0
class BaidutiebaItem(scrapy.Item):
    title = scrapy.Field()
    poster = scrapy.Field()
    post_time = scrapy.Field()
    content = scrapy.Field()
    follower = scrapy.Field()