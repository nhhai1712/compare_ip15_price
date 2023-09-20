import scrapy
from ip15_price_prediction.items import Ip15PricePredictionItem

class Ip15TgddSpider(scrapy.Spider):
    name = "ip15_tgdd"
    allowed_domains = ["www.thegioididong.com"]
    start_urls = ["https://www.thegioididong.com/dtdd-apple-iphone-15-series/"]

    def parse(self, response):
        products = response.css("div.container-productbox > ul > li a.main-contain")

        for product in products:
            item = Ip15PricePredictionItem()
            item['product_name'] = product.css("h3::text").get().strip()
            item['price'] = product.css("strong::text").get().strip()
            yield item

    # def parse_ip15(self, response):
    #     item = Ip15PricePredictionItem()
    #     item['product_name'] = response.css("div.container-productbox > ul > li a.main-contain > h3").extract_first()
    #     item['price'] = response.css("div.container-productbox > ul > li a.main-contain > strong").extract_first()

    #     yield item
