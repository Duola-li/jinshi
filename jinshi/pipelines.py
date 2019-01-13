# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class JinshiPipeline(object):
    def open_spider(self):
        self.file1 = open('jinshi.txt', 'a', encoding='utf-8')
    def process_item(self, item, spider):
        file2 = open('jinshi.txt', 'r', encoding='utf-8')
        s = file2.read()
        if s == '':
            self.file1.write(json.dumps(item, ensure_ascii=False) + '\n')
            self.file1.flush()
        elif s != '' and s.find(item['date']) == -1:
            print(item)
            self.file1.seek(0)
            self.file1.write(json.dumps(item, ensure_ascii=False) + '\n')
            self.file1.flush()
        return item
    def close_spider(self):
        self.file1.close()
