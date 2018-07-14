import scrapy
from bitcoinscraper.items import BitcoinscraperItem
from datetime import datetime
import re
import csv


class BitSpider(scrapy.Spider):
    name = "bitspider"
    start_urls = ['https://btc.com/block?date=2017-12-01']

    def parse(self, response):
        item = BitcoinscraperItem()  
        item['actualHeightOnly'] = response.xpath('/html/body/div/div/div[2]/div/div[2]/table/tr/td[1]/a/text()').extract()
        item['minerKnown'] = response.xpath('/html/body/div/div/div[2]/div/div[2]/table/tr/td[2]/div/a/text()').extract()
        
        next_page = response.xpath('/html/body/div/div/div[2]/div/div[3]/a[2]/@href').extract_first()

        end_page = 'https://btc.com/block?date=2018-02-01'
 
        if next_page != end_page :
            yield response.follow(next_page, callback = self.parse)
        
        zipItem = zip(*item.values())
        
        with open('minepool.csv', 'a', newline='') as f: 
            w = csv.writer(f)
            w.writerows(zipItem)

        yield item