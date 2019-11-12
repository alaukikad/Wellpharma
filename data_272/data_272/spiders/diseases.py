# -*- coding: utf-8 -*-
import scrapy
import csv


class DiseasesSpider(scrapy.Spider):
    name = 'diseases'
    allowed_domains = ['https://www.cdc.gov/diseasesconditions/az/']
    start_urls = [ 'http://www.cdc.gov/diseasesconditions/az/'+chr(x)+'.html' for x in range(97,123)]

    diseases = dict()
    def parse(self, response):
        print("Processing "+response.url)        

        extracted_data = response.xpath('//div[@class="az-content"]/ul/li/a/text()').extract()

        for i in range(len(extracted_data)):
            diseases = {i+1,extracted_data[i]}
            with open('diseases.csv','a') as f:
                f.write(f"{extracted_data[i]}\n")
            yield diseases  