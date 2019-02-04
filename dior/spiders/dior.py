import scrapy
import re, json

class DiorSpider(scrapy.Spider):
    name = 'dior'
    
    start_urls = ['https://www.dior.com/en_us']

    def parse(self, response):
        # follow links to author pages
        for href in response.css('a[class="navigation-item-link"]::attr(href)'):
            yield response.follow(href, self.parse_products)

        
    def parse_products(self, response):
        # follow links to author pages
        for href in response.css('a[class="product-link"]::attr(href)'):
            yield response.follow(href, self.parse_data)        



    def parse_data(self, response):
        b = r"(var dataLayer \= \[)(.*?)(\]\;\n)"
        a = response.css("script::text").getall()[2]
        m = re.findall(b, a, re.MULTILINE)[0][1]
        data = json.loads(m)
        
        yield {
            'name': data['ecommerce']['detail']['products'][0]['name'],
            'price': data['ecommerce']['detail']['products'][0]['price'],
            'currency': data['ecommerce']['currencyCode'],
            'category': data['topCategory'],
            'colour': data['ecommerce']['detail']['products'][0]['variant'],
            'country': data['country'],
            'time': response.request.meta['download_latency'],
            'SKU': data['ecommerce']['detail']['products'][0]['id'],
            'gender': data['subUniverse']
        }

