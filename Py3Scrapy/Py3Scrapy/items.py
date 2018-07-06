# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from .serializers import serializer_date


class Py3ScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field()
    zan = scrapy.Field()
    shoucang = scrapy.Field()
    pinglun = scrapy.Field()
    tags = scrapy.Field()
    font_image_url = scrapy.Field()
    font_image_path = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()


