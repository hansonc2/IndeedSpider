# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Job(scrapy.Item):
    title = scrapy.Field()
    employer = scrapy.Field()
    employer_link = scrapy.Field()
    location = scrapy.Field()
    salary = scrapy.Field()
    date = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
    pass
