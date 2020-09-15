#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import urllib.request
from bs4 import BeautifulSoup
import os

folder_path = './photo/'
if os.path.exists(folder_path) == False:  
    os.makedirs(folder_path)  
    
count = 0 #檔名計數

for page in range(0, 11): 
        headers = {
            'Connection': 'close',
        }
        web_content = requests.get(f'https://mdpr.jp/model/detail/1809?page={page}',headers=headers).text
        soup = BeautifulSoup(web_content, 'lxml')
    
        imgurl = []
        
        lists = soup.find_all('li', class_='media-e__item')

        allurl = []
        posturl = []
        
        for post in lists:
            title = post.find(['p','.media-e__p']).text #取得標題
            href = post.find('a')['href'] #取得連結
            date = post.find(['time','.media-e__sup']).text #取得日期
            print(title + '\n' + date + '\n' + 'https://mdpr.jp' + href ) #打印標題日期連結

            hrefmix = list(href)
            hrefmix.insert(-7, 'detail/') #加入展開全文的網址段
            hr = "".join(hrefmix)
            posturl = 'https://mdpr.jp' + hr
            dic = {}
            allurl.append(posturl)
 
            if allurl:
                url = allurl[-1]
                print(url)
                r = requests.get(url)
                web_content = r.text
                soup = BeautifulSoup(web_content, 'lxml')
                imgurl = soup.find_all('div', class_='figure')

                for img in imgurl:  
                    c = str(count)
                    i = img.find('img')['src']
                    okimg = i[0:-36] #去除webp副檔名
                    print(i) #打印圖片連結
                    urllib.request.urlretrieve(okimg, '/Users/hachibye/Downloads/Spyder_practice-master/photo/' + 'p' + c + okimg[-4:])
                    count += 1 #開頭的檔名計數
                    
                    