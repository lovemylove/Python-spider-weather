# -*-coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import string
target = 'http://www.tianqihoubao.com/lishi/xinxiang/month/201709.html'
pathname='D:/xinxiang.txt'

names=[]

def get_download_url():
        req = requests.get(url = target)
        html = req.text
        div_bf = BeautifulSoup(html)
        b = div_bf.find_all('b')
        for i in b[:4]:
            names.append(i.text)
            print i.text
#             writer(pathname, i.text.encode('utf8'))
        td = div_bf.find_all('td')
        for j in td[4:]:
            wea = "".join(string.strip(j.text).split())
            print wea
            names.append(wea)
        return names

def writer(pathname, li):
    count = 0
    with open(pathname,'a') as f:
#         f.write(li)
        for i in li:
            f.writelines(i.encode('utf8')+'  ')
            count = count + 1
            if count%4 == 0:
                f.write('\n')

if __name__ == '__main__':
    print 'start'
#     writer(pathname, li)
    writer(pathname,get_download_url())
    print 'end'
