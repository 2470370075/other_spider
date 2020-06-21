import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import os

r=requests.get('http://www.xiachufang.com/')
soup=BeautifulSoup(r.text)
imgs=soup.select('img')
imglist=[]
for i in imgs:
    if i.has_attr('data-src'):
        imglist.append(i.attrs['data-src'])
    else:
        imglist.append(i.attrs['src'])

img_path=os.path.join(os.curdir,'image')
if not os.path.isdir(img_path):
    os.mkdir(img_path)


for i in imglist:
    o=urlparse(i)
    filename=o.path[1:]

    filepath = os.path.join(img_path,filename)
    print(filepath)
    img_url = '%s://%s/%s' % (o.scheme, o.netloc, filename)
    if not img_url == ':///':
        img = requests.get(img_url)
        if  filepath != '.\image\simpleicons/sinaweibo.svg' and  filepath != '.\image\simpleicons/twitter.svg':
            with open('%s.jpg'%(filepath),'wb') as f:
                for i in img.iter_content(1024):
                    f.write(i)

