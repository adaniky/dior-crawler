import scrapy
import re, json

class DiorSpider(scrapy.Spider):
    name = 'dior'
    
    
    def start_requests(self):
        url = 'https://www.dior.com/'
        locate = getattr(self, 'locate', None)
        tags = [
                'fr_be', 
                'nl_be', 
                'de_de', 
                'es_es',
                'fr_fr',
                'it_it',
                'nl_nl',
                'ru_ru',
                'en_ch',
                'en_gb',
                'en_us',
                'pt_br',
                'es_sam',
                'zh_cn',
                'zh_hk',
                'en_hk',
                'ja_jp',
                'ko_kr',
                'zh_tw',
                ]
        if locate is not None:
            url = url + locate
            yield scrapy.Request(url, self.parse)
        else:
            for i in tags:
                url = url + i
                yield scrapy.Request(url, self.parse)
        

    def parse(self, response):
        
        for href in response.css('a[class="navigation-item-link"]::attr(href)'):
            yield response.follow(href, self.parse_products)

        
    def parse_products(self, response):
        
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
            'gender': data['subUniverse'],
            'description': response.css('meta[name="description"]::attr(content)').get()
        }

