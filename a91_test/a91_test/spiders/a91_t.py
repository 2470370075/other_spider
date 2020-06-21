# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request
import os
import re

class A91TSpider(scrapy.Spider):
    name = 'a91_t'
    allowed_domains = ['pic.workgreat17.live', 'pic.91p47.com', 'f.wonderfulday28.live']
    start_urls = ['https://f.wonderfulday28.live/forumdisplay.php?fid=19&filter=digest']
    c = 0

    def parse(self, response):
        posts = response.xpath('//tbody//a[contains(@style,"font-weight: bold;color: #8F2A90")]/@href').extract()
        for post in posts:
            post = 'https://f.wonderfulday28.live/' + post
            request = Request(post, self.parse_post)
            yield request

        pages = response.xpath('//div[@class="pages"]//a/@href').extract()
        for i in pages:
            page = 'https://f.wonderfulday28.live/' + i
            request = Request(page,self.parse)
            yield request

    def parse_post(self,response):
        img_urls = response.xpath('//img[@file]//@file').extract()
        for img_url in img_urls:
            if img_url[-3:] == 'gif':
                request = Request(img_url,self.img_download)
                yield request

    def img_download(self,response):
        self.c += 1
        path = os.path.abspath(os.curdir) + '/imgs'
        if not os.path.exists(path):
            os.makedirs(path)
        suffix = re.findall('\.\w+', response.url)[-1]
        name = str(self.c) + suffix
        with open('{}/{}.'.format(path,name),mode='wb') as f:
            f.write(response.body)