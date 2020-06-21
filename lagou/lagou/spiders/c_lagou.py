# -*- coding: utf-8 -*-

# 在首页点击label标签发送的请求和在搜索栏搜索发送的请求是不一样的，点击标签的话反爬措施很少

import scrapy
import re
from scrapy import Request


def get_cookies(cookies_string):
    cookies_string = '; ' + cookies_string + ';'
    keys = re.findall('; (.*?)=', cookies_string)
    values = re.findall('=(.*?);', cookies_string)
    cookies = dict(zip(keys, values))
    return cookies


import uuid

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

cookies = 'user_trace_token=20200425124743-5273d79b-f908-4845-88f5-27da30cb3ffc; _ga=GA1.2.2083221733.1587789941; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1587806295,1587825893,1587875701,1587876047; LGUID=20200425124744-fbc7ec26-70df-481f-8cba-75065f3fc714; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22171afa7e3597d-0f6e66ab39fcdd8-153a7440-1327104-171afa7e35a405%22%2C%22%24device_id%22%3A%22171afa7e3597d-0f6e66ab39fcdd8-153a7440-1327104-171afa7e35a405%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.jianshu.com%2Fgo-wild%3Fac%3D2%26url%3Dhttps%253A%252F%252Fwww.lagou.com%252Fjobs%252Flist_java%253FlabelWords%253D%2526fromSearch%253Dtrue%2526suginput%253D%253FlabelWords%253Dhot%22%2C%22%24latest_referrer_host%22%3A%22www.jianshu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; _gid=GA1.2.1384856302.1587789948; gate_login_token=0a4aee0e5c7cafb1a699e2443abb3a4d4f0466e01a6b3f99e42e3a27d54c4603; LG_LOGIN_USER_ID=b1a7924ce1c16abf4fa1de963adb72b38c2fcd7bf0eba3ffb9c05f5b54d7baa4; LG_HAS_LOGIN=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=255; index_location_city=%E5%85%A8%E5%9B%BD; privacyPolicyPopup=false; SEARCH_ID=bdb2a494207346de9e06672b3b9cd289; X_HTTP_TOKEN=37f5eccf3a1844ff982488785116e08ec86431237a; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1587884167; LGRID=20200426145809-7fdd1601-9421-433f-b2d1-4ae1326529ac; _putrc=2A0C4F15ECB073E1123F89F2B170EADC; JSESSIONID=ABAAAECAAEBABIIE3949A8E43314994E1700D7B433684DE; login=true; unick=%E7%8E%8B%E4%BD%B3%E5%85%B4; WEBTJ-ID=20200426123507-171b4c47b5e357-0dd6e5d3db1b6a8-153a7440-1327104-171b4c47b5f2cf; TG-TRACK-CODE=index_navigation; LGSID=20200426141251-d42ff762-98fb-4b17-8e6d-6a2ee8675b14; X_MIDDLE_TOKEN=c41be4d1bb03df35bfd38b5787826d02; _gat=1'

cookies2 = 'user_trace_token=20200425124743-5273d79b-f908-4845-88f5-27da30cb3ffc; _ga=GA1.2.2083221733.1587789941; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1587806295,1587825893,1587875701,1587876047; LGUID=20200425124744-fbc7ec26-70df-481f-8cba-75065f3fc714; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22171afa7e3597d-0f6e66ab39fcdd8-153a7440-1327104-171afa7e35a405%22%2C%22%24device_id%22%3A%22171afa7e3597d-0f6e66ab39fcdd8-153a7440-1327104-171afa7e35a405%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.jianshu.com%2Fgo-wild%3Fac%3D2%26url%3Dhttps%253A%252F%252Fwww.lagou.com%252Fjobs%252Flist_java%253FlabelWords%253D%2526fromSearch%253Dtrue%2526suginput%253D%253FlabelWords%253Dhot%22%2C%22%24latest_referrer_host%22%3A%22www.jianshu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; _gid=GA1.2.1384856302.1587789948; gate_login_token=0a4aee0e5c7cafb1a699e2443abb3a4d4f0466e01a6b3f99e42e3a27d54c4603; LG_LOGIN_USER_ID=b1a7924ce1c16abf4fa1de963adb72b38c2fcd7bf0eba3ffb9c05f5b54d7baa4; LG_HAS_LOGIN=1; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=255; index_location_city=%E5%85%A8%E5%9B%BD; privacyPolicyPopup=false; SEARCH_ID=8177ed2437df4ccb95bff104702dc2da; X_HTTP_TOKEN=37f5eccf3a1844ff379488785116e08ec86431237a; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1587884852; LGRID=20200426150933-d6823d64-b6ea-47d6-9d60-6ad1e3e52756; _putrc=2A0C4F15ECB073E1123F89F2B170EADC; JSESSIONID=ABAAAECAAEBABIIE3949A8E43314994E1700D7B433684DE; login=true; unick=%E7%8E%8B%E4%BD%B3%E5%85%B4; WEBTJ-ID=20200426123507-171b4c47b5e357-0dd6e5d3db1b6a8-153a7440-1327104-171b4c47b5f2cf; TG-TRACK-CODE=index_navigation; LGSID=20200426141251-d42ff762-98fb-4b17-8e6d-6a2ee8675b14; X_MIDDLE_TOKEN=c41be4d1bb03df35bfd38b5787826d02; _gat=1'


def html(response):
    with open('{}.html'.format(response.url[8:].replace('.', '').replace('/', '').replace('?', '').replace('=', '')),
              'w', encoding='utf-8') as f:
        f.write(response.text)


class LagouSpider(scrapy.Spider):
    name = 'c_lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/zhaopin/Python/?labelWords=label']

    def parse(self, response):
        Cookie = response.request.headers.getlist('Cookie')
        print('111111',Cookie)
        html(response)
        cookie = get_cookies(cookies)
        import time
        time_stamp2 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        LGRID = time_stamp2 + '-' + str(uuid.uuid1())
        cookie['LGRID'] = LGRID
        jobs = response.xpath('//div[@class="p_top"]//h3/text()').extract()
        salary = response.xpath('//div[@class="p_bot"]//span[@class="money"]/text()').extract()
        pages = response.xpath('//div[@class="pager_container"]//a[@class="page_no"]/@href').extract()
        res = list(zip(jobs, salary))
        next_page = re.findall(r'a href="(.*)" class="page_no"', response.text)
        print(res)

        yield Request(url=next_page[-1],
                      callback=self.parse,
                      cookies=cookie,
                      headers=headers
                      )

        jobs = response.xpath('//div[@class="list_item_top"]//div[@class="p_top"]//a/@href').extract()
        print(jobs)
    #
        for i in jobs:
            yield Request(url=i,
                          callback=self.job_parse,

                          headers=headers,
                            cookies = cookie,
                          )

    def job_parse(self, response):
        Cookie = response.request.headers.getlist('Cookie')
        html(response)
