# dior-crawler
To carry out academic researches sometimes it`s necessary to have a constantly maintained base of all products from online shopping sites. For such purposes, [the Scrapy](https://docs.scrapy.org) framework is great
My simple scraper of site "https://www.dior.com" based on Python 3.7.1 and Scrapy 1.6.0 
To run this app enter to shell: 
```
pip install -r requirements.txt
scrapy crawl dior -o dior.csv
```
The file named "dior.csv" will appear in your base directory. Scrapy App will collect all products in all categories of the site and write to this file. Downloaded data array consists of such columns:
* name - The product name
* price - The product price
* currency - Сurrency in which the price is presented
* category - The product category
* colour - The product colour
* country - The region in which the product is available
* time - Time of the one product parsing 
* SKU - The Product Stock Keeping Unit 
* gender - Сategory for which the product is intended
* description - Product description

To scrape all products in one some region, print in shell:
```
scrapy crawl dior -o dior.csv -a locate="some_region_language_code"
```
for example for all products that are available in Germany print in shell:
```
scrapy crawl dior -o dior.csv -a locate=de_de
```
Where de_de - German Language Code

The list of all available language codes is in the file "alternate.txt"
If you will type in shell this one:
```
scrapy crawl dior -o dior.csv -a locate=de_de
```
you`ll get quantity of products and percentage of products by category, colour, country, gender and currency as a file "test.json"

