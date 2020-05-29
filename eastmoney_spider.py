# -*-coding:utf-8-*-

import requests
from lxml import etree
from spider_mongo import collection
import re

url = 'http://fund.eastmoney.com/news/cjjyw_1.html'
#
headers = {
        'USER-AGENT':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

response = requests.get(url=url, headers = headers)
html = response.text

html_element = etree.HTML(html)

detail_url_pre = 'http://fund.eastmoney.com/a/'
# 获取详情页面的url
source_urls = html_element.xpath('/html/body/div[6]/div[2]/div[1]/div/div[1]/div/ul/li/a/@href')
num = 0
for source_url in source_urls:
    # 以详情页作为mongo去重的id
    status_Id = source_url
    detail_url = detail_url_pre + source_url
    response = requests.get(url=detail_url, headers = headers).text
    response_detail = etree.HTML(response)
    # title:标题  digest：摘要  content:内容 img：图片
    title = response_detail.xpath('/html/body/div[1]/div[4]/div[1]/div[2]/div[1]/h1/text()')[0]
    print(title)
    digest_xpath = response_detail.xpath('//*[@id="ContentBody"]/div[2]/text()')
    digest = digest_xpath[0] if digest_xpath else None
    print(22222222,digest)
    content_text = response_detail.xpath('//*[@id="ContentBody"]/p[3]/strong/text() | //*[@id="ContentBody"]/p//text()')
    content = ''.join(content_text)
    print(content)
    img = response_detail.xpath('//*[@id="ContentBody"]/center/img/@src | //*[@id="ContentBody"]/p/a/img/@src')
    print(img)
    date_time = response_detail.xpath('/html/body/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/text()')
    print(date_time)
    # 向mongo中添加数据(重复就不添加)
    data = {'title':title, 'digest':digest, 'content':content, 'img':img, 'date_time':date_time, 'status_Id':status_Id}
    status_id = collection.count_documents({'status_Id':status_Id})
    print(1111111111111,status_id)
    collection.update({'status_Id':status_Id},{'$set':data}, upsert= True)






