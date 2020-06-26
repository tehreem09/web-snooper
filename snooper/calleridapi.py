#!/usr/bin/env python3

import requests
import scrapy

# class PostsSpider(scrapy.Spider):
#     pass
url = "https://www.zabasearch.com"
header = {'Host': 'www.zabasearch.com',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://www.zabasearch.com/',
'DNT': 1,
'Connection': 'keep-alive',
'Cookie': 'datadome=HS-XuHO1a_i-8vN_q3MK.031HWTOxmHI.Si7KirSBb5N~YNahwN0Cnm-7weABfL.2bxZSWAG-wUfko4FMJYVObElYecH4WZQ7UMZHT5UNM; PHPSESSID=tmfs1e7cntuhp5jqovuj5115a0; TS01b4987e=01b52ee1781a0791ba08d7ffbc9ab20074d6f98e768dde6a8cffc551c1b60ba4628fb25b57aef596809324da6f9f59448e90be2d6b; TS0111e5d9=01b52ee178ce783300c5aa96180f72494a80f9c116b7b5a54d987cf2b0a44572a645403dd115866bf3fb467c3af66439e134292ba5; CUID=N,1590179711753:ALHGLuQAAAAPTiwxNTkwMTc5NzExNzUza5WC0HsZvI4iaU6ZZnuvEumsnHtPwpAX+fXnGhAwd9vwZDkMzFdeiHq/tALQDmyPJ0i7LSJdLEVViguuzk5apfxR93UndrZ34Qj4p5Z67rIv+E/6q7ybbbV3hz425a5mDc4tfGLAxXX1aRX/+HHBAe6OgB/2CYTNgB6YlHVG3NddDMkpbr3Pi9OwXrkoKkwvFTQ7AAzJSMmqjUB9MwYo/FIqtAJCiern9Oi6V50cdhP4/i3PHVIQ3bb+IXJn1vPhnLe8kofkHEaQAE6P7b66QJ2suP/o2qiWVYr8dmeYBOj3gLSdHuPv5R5AR+ey0I2iTbYxj79b+T+oEG1ABD9l/A==; FCCDCF=[["AKsRol_KEPPUSwqPSNBFzOh2pRKnSLnvnonpLpKOniyzPVoy5IsYBIacx9RRpNLbLvbs7zHNfWQkRPXP3fqfvdeQVheEm_LUm-MT-M9kOvxxBKaQOLISmeuqippKTzyLXZ2wrfGEgHozm6jPl0hszIOx4xTcGIKliQ=="],null,["[[],[],[],[],null,null,true]",1590179728158]]',
'Upgrade-Insecure-Requests': 1}

# response = requests.get(url, header)
# print(response.status_code)

# from opencnam import Phone

# url = "https://veriphone.p.rapidapi.com/verify"
#
# querystring = {"phone":"%2B4915123577723"}
#
# headers = {
#     'x-rapidapi-host': "veriphone.p.rapidapi.com",
#     'x-rapidapi-key': "f75c8f38f1msha318a7f156c348dp12dc0ajsnc6196b38f2d4"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)
# print()
# # phone = Phone('+16284003994')
# phone = Phone("+16284003994", account_sid="AC021", auth_token="AU529")
# print (phone.number, phone.cnam)

# s = requests.Session()

# s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})

# url = "https://facebook.com/"
# s = requests.Session()
# s.auth = ('tehreem973', 'shaklana08012001++htf')
# s.headers.update({'x-test': 'true'})
# print(s.head('https://wwww.facebook.com/tehreem973'))