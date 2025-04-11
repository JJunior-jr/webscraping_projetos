import scrapy


class NotbookSpider(scrapy.Spider):
    name = "notbook"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/notebook#D[A:notebook]"]

    def parse(self, response):
        pass
