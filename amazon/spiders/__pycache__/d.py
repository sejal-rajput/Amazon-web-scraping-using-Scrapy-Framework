# -*- coding: utf-8 -*-
import scrapy


class ASpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.com.au']
    start_urls = ['https://www.amazon.com.au/Shorts-Clothing/s?rh=n%3A5130960051&page=1']

    def parse(self, response):
    	urls = response.xpath('//*[@class="s-result-item s-result-card-for-container a-declarative celwidget  "]') 
    	for url in urls:
    		product_name = url.xpath('.//*[@class="a-size-base s-inline s-access-title a-text-normal"]/text()').extract()
    		product_price = url.xpath('.//*[@class="a-size-base a-color-price s-price a-text-bold"]/text()').extract()
    		product_rating = url.xpath('.//*[@class="a-icon-alt"]/text()').extract()
    		people_rated = url.xpath('.//*[@class="a-size-small a-link-normal a-text-normal"]/text()').extract()
    		
    		yield{'product_name' : product_name,
    			  'product_price' : product_price,
    			  'product_rating' : product_rating,
    			  'people_rated' : people_rated}

    	np = response.xpath("//*[@class='pagnNext']/@href").get()
    	if np is not None:
    		ap = response.urljoin(np)
    		yield scrapy.Request(ap,callback=self.parse,dont_filter=True)