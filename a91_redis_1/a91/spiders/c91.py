# -*- coding: utf-8 -*-

# https://www.cnblogs.com/pythoner6833/p/9148937.html 很好的介绍网址
# redis里面lpush一个网址，开几个scrapy爬
# lpush start_url          scrapy crawl c91_redis_1
# linux连接redis：用redis客户端redis-cli -h 172.xx.xx.xx
import scrapy
from scrapy import Request
import os
import re
from scrapy_redis.spiders import RedisSpider

class C91Spider(RedisSpider):

    name = 'c91_redis_1'
    allowed_domains = [ 'pic.workgreat15.live','pic.workgreat14.live','pic.workgreat17.live','pic.91p47.com','f.wonderfulday28.live']
    # start_urls = ['https://f.wonderfulday28.live/forumdisplay.php?fid=19&filter=digest']
    redis_key = "start_url"
    c = 0

    def parse(self, response):
        posts = response.xpath('//tbody//a[contains(@style,"font-weight: bold;color: #8F2A90")]/@href').extract()
        for post in posts:
            post = 'https://f.wonderfulday28.live/' + post
            request = Request(post,self.parse_post)
            yield request

        pages = response.xpath('//div[@class="pages"]//a/@href').extract()
        for i in pages:
            page = 'https://f.wonderfulday28.live/' + i
            request = Request(page,self.parse)
            yield request

    def parse_post(self,response):
        img_urls = response.xpath('//img[@file]//@file').extract()
        for img_url in img_urls:
            if img_url[-3:] == 'gif':            #只下载gif
                request = Request(img_url,self.img_download)
                yield request

    def img_download(self,response):
        self.c += 1
        path = os.path.abspath(os.curdir) + '/imgs'
        if not os.path.exists(path):
            os.makedirs(path)
        suffix = re.findall('\.\w+', response.url)[-1]
        name = str(self.c) + response.url[-18:-5] + suffix
        with open('{}/{}.'.format(path,name),mode='wb') as f:
            f.write(response.body)



