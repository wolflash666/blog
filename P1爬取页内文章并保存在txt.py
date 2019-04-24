from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import urllib.request
#import os
#import requests

url="http://www.duanmeiwen.com/zhuanti/44819.html"
#url= requests.get(url).content.decode('gb2312','ignore')
try:
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/52.0.2743.116'}
    req=urllib.request.Request(url,headers=headers)
    data=urllib.request.urlopen(req).read().decode('gb2312','ignore')#解码防错加了“ignor”
    dammit=UnicodeDammit(data,["utf-8"])
    data=dammit.unicode_markup
    soup=BeautifulSoup(data,"lxml")
    soups=soup.find_all("p")
    heti=""
    for soup in soups:
        heti=heti+soup.text
    f=open('1.txt','w')
    f.write(heti)
    f.close()
    print("爬取成功！")

except Exception as err:
    print(err)
