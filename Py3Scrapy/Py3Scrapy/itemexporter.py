# -*- coding: utf-8 -*-

import json
from scrapy.exporters import JsonItemExporter, BaseItemExporter

class ArticleJsonItemExporter(JsonItemExporter):

    def serialize_field(self, field, name, value):
        if name == "create_date":
            return value.strftime('%Y/%m/%d')
        return super().serialize_field(field, name, value)

class ArticleJsonWithEncodingItemExporter(BaseItemExporter):

    def __init__(self, file, **kwargs):
        self.file = file
        super().__init__(**kwargs)

    def export_item(self, item):
        itemdict = dict(self._get_serialized_fields(item))
        line = json.dumps(itemdict) + '\n'
        self.file.write(line)
        pass

    def serialize_field(self, field, name, value):
        if name == "create_date":
            return value.strftime('%Y/%m/%d')
        return super().serialize_field(field, name, value)