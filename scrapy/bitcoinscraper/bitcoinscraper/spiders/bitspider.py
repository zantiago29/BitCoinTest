import scrapy
from bitcoinscraper.items import BitcoinscraperItem
from datetime import datetime
import re
import csv


class BitSpider(scrapy.Spider):
    name = "bitspider"
    start_urls = ['https://bitcoinchain.com/block_explorer/2017-12-01-2018-01-31']


    def parse(self, response):
        item = BitcoinscraperItem()
        item['height'] =  response.xpath('/html/body/div[1]/div[2]/div/div/div[4]/div/table/tr/td/a/text()').extract()  
        #item['actualHeightOnly'] = response.xpath('/html/body/div[1]/div[2]/div/div/div[4]/div/table/tr/td[@class="num"]/a/text()').extract() 
        #item['minerUnkown] = response.xpath('/html/body/div[1]/div[2]/div/div/div[4]/div/table/tr[@class="b-blocks__elem "]/td[@class="text-right"]/a/text()').extract()
        #item['minerKnown] = response.xpath('/html/body/div[1]/div[2]/div/div/div[4]/div/table/tr[@class="b-blocks__elem "]/td[@class="text-right"]/text()').extract()
        
        itemsTotal = len(item['height'])
        f = 2
        itemDict = {}

        for entry in range(itemsTotal-4):
            itemDict[item['height'][entry]] = item['height'][f]
            entry +=3
            f = entry + 2
        with open('minepool.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in itemDict.items():
                writer.writerow([key, value])
        
        yield item