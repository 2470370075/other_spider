# -*- coding: utf-8 -*-
import scrapy
from qianmu_pipl.items import QianmuPiplItem

class QianmuPSpider(scrapy.Spider):
    name = 'qianmu_p'
    allowed_domains = ['www.qianmu.org']
    start_urls = ['http://www.qianmu.org/ranking/1528.htm']

    def parse(self, response):
        u = response.xpath('//colgroup/following-sibling::tbody[1]/tr[position()>1]/td[2]/a/@href').extract()
        print('qianmu_p')
        print(u)
        print("总共爬取{}个页面。".format(len(u)))
        for link in u:
            yield response.follow(link,self.u_parse)

    def u_parse(self,response):
        item = QianmuPiplItem()
        response=response.replace(body=response.text.replace('\t',''))
        k = response.xpath('//div[@id="wikiContent"]/div[@class="infobox"]/table/tbody[1]/tr/td[1]').xpath("string(.)").extract()
        v = response.xpath('//div[@id="wikiContent"]/div[@class="infobox"]/table/tbody[1]/tr/td[2]').xpath("string(.)").extract()
        n = response.xpath('//h1[@class="wikiTitle"]/text()').extract_first()
        dic = {'name': n}
        if len(k) == len(v):
            for i in range(len(k)):
                dic[k[i].replace('\t','')] = v[i].replace('\t','')
            print(dic)
        item['name'] = dic.get('name')
        item['rank'] = dic.get('排名')
        yield item