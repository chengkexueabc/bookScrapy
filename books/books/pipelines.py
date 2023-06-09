# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class BooksPipeline:
#     def process_item(self, item, spider):
#         return item
class PriceConverterPipeline(object):

    exchange_rate = 8.8075

    def process_item(self, item, spider):
        price = float(item['price'][1:]) * self.exchange_rate
        item['price'] = '¥%.2f' % price
        return item
