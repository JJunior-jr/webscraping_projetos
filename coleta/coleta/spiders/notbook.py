import scrapy


class NotbookSpider(scrapy.Spider):
    name = "notbook"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/notebook#D[A:notebook]"]

    def parse(self, response):

        products= response.css("div.ui-search-result__wrapper ") #ui-search-result__wrapper--large

        for product in products:
            
            prices = product.css("span.andes-money-amount__fraction::text").getall()
            
            yield { # o return retorna um item e o yield retorna um gerador, o que é mais eficiente
                           
                "brand": product.css("span.poly-component__brand::text").get(),
                "name": product.css("a.poly-component__title::text").get(),
                "seller": product.css("span.poly-component__seller::text").get(),
                "reviw_rating_number": product.css("span.poly-reviews__rating::text").get(),
                "review_amount": product.css("span.poly-reviews__total::text").get(),
                "old_money": prices[0] if len(prices) > 0 else None,
                "new_money": prices[1] if len(prices) > 0 else None
                #"title": produc"t.css("ui-search-result__title").get(),""
                #"price": product.css("ui-search-result__price").get(),
                #"link": product.css("ui-search-result__link").get(),
            }
        pass
