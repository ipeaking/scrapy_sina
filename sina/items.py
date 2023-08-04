# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class GuoneiItem(scrapy.Item):
    title = scrapy.Field()
    desc = scrapy.Field()
    times = scrapy.Field()


class ZongyiItem(scrapy.Item):
    title = scrapy.Field()
    desc = scrapy.Field()
    times = scrapy.Field()


class DataItem(scrapy.Item):
    title = scrapy.Field()
    desc = scrapy.Field()
    times = scrapy.Field()
    type = scrapy.Field()
