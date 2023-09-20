import scrapy


class Ip15PricePredictionItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field()
    price = scrapy.Field()
