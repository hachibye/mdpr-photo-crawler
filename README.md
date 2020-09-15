# mdpr-photo-crawler
 
## modelpress 日本新聞網站爬蟲

###### https://mdpr.jp/

#### 用途：根據對象一次打包圖片，爬蟲練習用，代碼簡易

###### ＊＊＊請勿用於非法用途＊＊＊

<br>
<br>


* 填空1. 修改頁數範圍
```
for page in range(0, 11): 
```

* 填空2. 修改爬取網址
```
web_content = requests.get(f'https://mdpr.jp/model/detail/1809?page={page}',headers=headers).text
```

* 填空3. 修改存放路徑
```
urllib.request.urlretrieve(okimg, '/Users/hachibye/photo/' + 'p' + c + okimg[-4:])
```

<br>
<br>

* 關於爬取網址

可以是搜尋結果頁面（較不精確）也可以是人物頁面（較為精確）

![ps1](https://i.imgur.com/n4e9GbP.png "搜尋結果頁面")

![ps2](https://i.imgur.com/RfHRagD.png "搜尋結果頁面")
