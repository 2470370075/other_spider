# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

#
class QianmuSpider(scrapy.Spider):
    name = 'qianmu'
    allowed_domains = ['www.qianmu.org']
    start_urls = ['http://www.qianmu.org/ranking/1528.htm']

    def parse(self, response):
        u = response.xpath('//colgroup/following-sibling::tbody[1]/tr[position()>1]/td[2]/a/@href').extract()

        print("总共爬取{}个页面。".format(len(u)))
        for link in u:
            request = Request(link,self.u_parse)

            yield request

    def u_parse(self,response):
        response=response.replace(body=response.text.replace('\t',''))
        k = response.xpath('//div[@id="wikiContent"]/div[@class="infobox"]/table/tbody[1]/tr/td[1]').xpath("string(.)").extract()
        v = response.xpath('//div[@id="wikiContent"]/div[@class="infobox"]/table/tbody[1]/tr/td[2]').xpath("string(.)").extract()
        n = response.xpath('//h1[@class="wikiTitle"]/text()').extract_first()
        dic = {'name': n}
        if len(k) == len(v):
            for i in range(len(k)):
                dic[k[i].replace('\t','')] = v[i].replace('\t','')
            print(dic)
            with open("info.txt", mode='a', encoding='utf-8', ) as f:
                f.write(str(dic) + "\n")
