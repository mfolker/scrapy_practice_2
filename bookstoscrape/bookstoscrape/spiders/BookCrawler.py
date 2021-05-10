import codecs
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from bookstoscrape.items import BookstoscrapeItem

class BookcrawlerSpider(CrawlSpider):
    name = 'BookCrawler'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow=r'catalogue/category'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        book = BookstoscrapeItem()

        books = response.xpath('//article[@class="product_pod"]')

        for b in books: 
            book['title'] = b.xpath('.//h3/a/@title').extract_first()
            book['price'] = b.xpath('.//div/p[@class="price_color"]/text()').extract_first()
            
            #Imageurl and book url

            with codecs.open('results/books.txt', 'a+', 'utf-8',) as f:
                f.write(book['title'] + '\r\n')
                f.write(book['price'] + '\r\n\r\n')
