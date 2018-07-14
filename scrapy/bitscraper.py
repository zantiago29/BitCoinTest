import scrapy

class bitcoinSpider(scrapy.Spider):
    name = "bitcoin_scraper"
    start_urls = ['https://btc.com/000000000000000000a582aba3845a060f2e0eb9136b386ec88fa1acccfbd49b']