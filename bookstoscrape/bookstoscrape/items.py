import scrapy


class BookstoscrapeItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    imageurl = scrapy.Field()
    bookurl = scrapy.Field()
