# -*-coding:utf-8-*-

# # AppKey：203815481     AppSecret：dfw16farchiz962hvj79usq4libx7q2n
# # AppCode：d865036d93804f61a5ca9db2614a525a

import urllib.request, sys
from urllib.parse import urlencode
import requests
import ssl


host = 'https://iweather.market.alicloudapi.com/address'
appcode = 'd865036d93804f61a5ca9db2614a525a'
area = '西湖'
city = '杭州'
prov = '浙江'
query_arg = {
    'area': area, 'city':city,
    'needday':1, 'prov':prov
}
query_str = urlencode(query_arg)
url = host + '?' + query_str

r = requests.get(url, headers={
    'Authorization': 'APPCODE ' + appcode
}, verify=False)
print(r)
print(r.json())


