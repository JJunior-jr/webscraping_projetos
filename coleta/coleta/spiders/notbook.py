import scrapy


class NotbookSpider(scrapy.Spider):
    name = "notbook"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/notebook#D[A:notebook]"]

    def parse(self, response):

        products= response.css("div.ui-search-result__wrapper ") #ui-search-result__wrapper--large

        for product in products:
            yield { # o return retorna um item e o yield retorna um gerador, o que é mais eficiente
                
                "brand": product.css("span.poly-component__brand::text").get(),
                "name": product.css("a.poly-component__title::text").get(),
                #"title": produc"t.css("ui-search-result__title").get(),""
                #"price": product.css("ui-search-result__price").get(),
                #"link": product.css("ui-search-result__link").get(),
            }
        pass
