# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PriceConverterPipeline(object):

    #英镑兑换人民币汇率
    exchange_rate = 8.77

    def process_item(self, item, spider):
        price = float(item['price'][1:]) * self.exchange_rate

        #保留2位小数
        item['price'] = '￥%.2f' % price
        return item
