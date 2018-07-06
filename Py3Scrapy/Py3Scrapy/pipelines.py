# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
from .itemexporter import ArticleJsonItemExporter, ArticleJsonWithEncodingItemExporter


class Py3ScrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class ArticleImagesPipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        if results[0][0]:
            item['font_image_path'] = results[0][1]['path']
        return item


class JsonWithEncodingPipeline(object):

    def __init__(self):
        #codecs可以解决编码问题，会自动统一转化成unicode
        self.file = codecs.open('article.json', 'w', encoding='utf-8')
        self.exporter = ArticleJsonWithEncodingItemExporter(self.file, encoding='utf-8')

    def process_item(self, item, spider):
        #json.dumps()于将dict类型的数据转成str
        # json.dump()用于将dict类型的数据转成str，并写入到json文件中。
        #json.loads()用于将str类型的数据转成dict
        # json.load()用于从json文件中读取数据。
        # line = json.dumps(dict(item)) + '\n'
        # self.file.write(line)
        #使用自定义JSONexporter
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

class JsonExporterPipeline(object):

    def __init__(self):
        self.file = open('articleexport.json', 'wb')
        self.exporter = ArticleJsonItemExporter(self.file, encoding= 'utf-8', ensure_ascii= False)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


class MysqlTwistedPipline(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_crawler(self, crawler):
        pass

    def process_item(self, item, spider):
        return item