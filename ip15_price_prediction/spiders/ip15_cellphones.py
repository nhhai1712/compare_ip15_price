import scrapy
from ip15_price_prediction.items import Ip15PricePredictionItem

class Ip15CellphonesSpider(scrapy.Spider):
    name = "ip15_cellphones"
    allowed_domains = ["cellphones.com.vn"]
    start_urls = ["https://cellphones.com.vn/mobile/apple/iphone-15.html/"]

    def parse(self, response):
        
        products = response.css("div.swiper-wrapper > div > div > a")
        print("/n")
        print(products)
        print("/n")
        for product in products:
            item = Ip15PricePredictionItem()
            item['product_name'] = product.css("h3.c-product-item__title a::text").get().strip()
            item['price'] = product.css("div.c-product-item__price span::text").get().strip()
            yield item

    # def parse_ip15(self, response):
    #     item = Ip15PricePredictionItem()
    #     item['product_name'] = response.css("div.swiper-container.list-product-swiper.swiper-container-initialized.swiper-container-horizontal > div.swiper-wrapper > div.swiper-slide.swiper-slide-active > div > div > a > div.product__name > h3").extract_first()
    #     item['price'] = response.css("div.swiper-container.list-product-swiper.swiper-container-initialized.swiper-container-horizontal > div.swiper-wrapper > div.swiper-slide.swiper-slide-active > div > div > a > div.last-price > span").extract_first() 
    #     yield item
