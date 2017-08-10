# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RecipescraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    author = scrapy.Field()
    ingredients = scrapy.Field()
    recipeyield = scrapy.Field()
    totaltime = scrapy.Field()
    activetime = scrapy.Field()
    directions = scrapy.Field()
    difficulty = scrapy.Field()