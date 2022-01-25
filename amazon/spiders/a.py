# -*- coding: utf-8 -*-
import scrapy


class ASpider(scrapy.Spider):
    name = 'a'
    allowed_domains = ['www.amazon.com.au']
    start_urls = ['https://www.amazon.com.au/s?rh=n%3A4851856051%2Cn%3A%214851857051%2Cn%3A5130734051%2Cn%3A5130763051%2Cn%3A5130960051&page=2&qid=1588909132&ref=lp_5130960051_pg_2']

    def parse(self, response):
    	urls = response.xpath('//*[@class="s-result-list s-search-results sg-row"]')
    	for url in urls:
    		product_name = url.xpath('.//*[@class="a-size-base-plus a-color-base a-text-normal"]/text()').extract()
    		product_price = url.xpath('.//*[@class="a-price-whole"]/text()').extract()
    		product_rating = url.xpath('.//*[@class="a-icon-alt"]/text()').extract()
    		people_rated = url.xpath('.//*[@class="a-size-base"]/text()').extract()
    		product_imglink = url.xpath('//*[@class="s-image"]/@src').extract()

    		yield{'product_name' : product_name,
    			  'product_price' : product_price,
    			  'product_rating' : product_rating,
    			  'people_rated' : people_rated,
                  'product_imglink' : product_imglink}

    	np = response.xpath('//*[@class="a-last"]/a/@href').extract_first()
    	if np:
    		ap = response.urljoin(np)
    		yield scrapy.Request(ap,callback=self.parse)