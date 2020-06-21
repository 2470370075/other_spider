import requests
from lxml import etree
import threading
from queue import Queue

# 多线程爬取，思路：
# 把需要爬取的页面先全部放入一个队列，创建5个线程，
# 去队列里不停的（While Ture）取url并下载，（download）
# 取光之后(queue.join())放入5个None，
# 线程取到None跳出循环并结束。

def parse(i):
    u_info = requests.get(i)
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
        link=links.get()
        if link == None:
            break
        parse(link)
        links.task_done()
        global count
        count += 1
        print("第{}个页面。".format(count))

if __name__ == '__main__':
    count=0
    res = requests.get('http://www.qianmu.org/ranking/1528.htm')
    selector = etree.HTML(res.text)
    u = selector.xpath('//colgroup/following-sibling::tbody[1]/tr[position()>1]/td[2]/a/@href')
    print("总共爬取{}个页面。".format(len(u)))

    links = Queue()
    for i in u:
        links.put(i)

    for i in range(50):
        t = threading.Thread(target=download)
        t.start()

    links.join()
    for i in range(50):
        links.put(None)


