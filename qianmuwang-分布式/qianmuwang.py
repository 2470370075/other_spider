import requests
from lxml import etree
import threading
import redis

#分布式：多个地方的程序一起完成一个爬取任务
#思路：for i in 要爬的url，添加到redis集合，
#      如果可以添加进去说明首次添加没爬过，起校验功能
#      再放到队列里去供自己和其他人下载

def parse(i):
    print(i)
    u_info = requests.get(i,timeout=60)
    u_info_selector = etree.HTML(u_info.text.replace('\t', ''))
    k = u_info_selector.xpath('//div[@id="wikiContent"]/div[@class="infobox"]/table/tbody[1]/tr/td[1]')
    v = u_info_selector.xpath('//div[@id="wikiContent"]/div[@class="infobox"]/table/tbody[1]/tr/td[2]')
    n = u_info_selector.xpath('//h1[@class="wikiTitle"]/text()')
    dic = {'name': n}
    if len(k) == len(v):
        for i in range(len(k)):
            dic[k[i].xpath("string(.)")] = v[i].xpath("string(.)")
        print(dic)
        with open("info.txt" , mode='a', encoding='utf-8', ) as f:
            f.write(str(dic) + "\n")

def download():
    while True:
        link = r.rpop('links_queue')                          #空转
        parse(link)

if __name__ == '__main__':
    r=redis.Redis(host="192.168.241.135",port=6379)

    res = requests.get('http://www.qianmu.org/ranking/1528.htm')
    selector = etree.HTML(res.text)
    u = selector.xpath('//colgroup/following-sibling::tbody[1]/tr[position()>1]/td[2]/a/@href')

    for link in u:
        if r.sadd('links_seen',link):
            r.lpush('links_queue',link)


    for i in range(5):
        t = threading.Thread(target=download)
        t.start()



