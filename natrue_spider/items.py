# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NatrueSpiderItem(scrapy.Item):
    # define the fields for your item here like:
	name = scrapy.Field()
	university = scrapy.Field()
	money = scrapy.Field()
	numb = scrapy.Field()
	style = scrapy.Field()
	school = scrapy.Field()
	year = scrapy.Field()
	
