# -*- coding: utf-8 -*-
import re
import scrapy,time


class DataSpider(scrapy.Spider):
    name = 'data'
    allowed_domains = ['jin10.com']
    start_urls = ['https://www.jin10.com/']

    def parse(self, response):
        times = response.xpath('//div[@class="jin-flash_h"]/div[@class="jin-flash_icon"]/a/@href').extract()
        infos = [info.xpath('string(.)').extract_first() for info in response.xpath('//div[@class="jin-flash_b"]')]


        # print(date,times)
        date_list = []
        for time1 in times:
            if time1:
                s = re.match(r'//view.jin10.com/news(\d{14})', time1)

                date_list.append(s.group(1))
        # print(date_list)
        for date,info in zip(reversed(date_list),reversed(infos)):

            yield {'date':date,'info':info}

        yield scrapy.Request('https://www.jin10.com/',dont_filter=True)
