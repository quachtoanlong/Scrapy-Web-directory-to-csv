# -*- coding: utf-8 -*-
import scrapy


class GettheprofDictSpider(scrapy.Spider):
    name = 'gettheprof_dict'
    allowed_domains = ['bizfaculty.nus.edu.sg']
    start_urls = ['http://bizfaculty.nus.edu.sg/faculty-directory/page/1/']

    def parse(self, response):
        
        print("processing: " + response.url)
        
        for prof in response.css('div.cards-details'):
            scraped_info = {
                'name'      : prof.css("div.cards-details h4 a::text").extract()[0].strip(),
                'position'  : prof.css("div.cards-details div span::text").extract(),
                'department': prof.css("div.cards-details div strong::text").extract()[0].strip(),
                'location'  : prof.css("ul.cards-contact li:nth-child(1) div::text").extract(),
                'phone'     : prof.css("ul.cards-contact li:nth-child(2) div::text").extract(),
                'email'     : prof.css("ul.cards-contact li:nth-child(3) div a::text").extract(),                
            }


            #yield or give the scraped info to scrapy
            yield scraped_info

            i = 2
            for i in range(25):
                yield scrapy.Request(
                response.urljoin('http://bizfaculty.nus.edu.sg/faculty-directory/page/' + str(i)),
                callback=self.parse)
                i+= 1