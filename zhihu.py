#!/usr/bin/python2
# -*- coding:utf-8 -*-
import urllib2
import cookielib
import urllib
cookie = cookielib.CookieJar()
cookie_p = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(cookie_p)
urllib2.install_opener(opener)
baseurl = 'http://210.33.28.180/biyesheng/default.aspx'
headers = {
    #'Accept': #'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    #'Host':'210.33.28.180',
    #'Origin':'https://210.33.28.180',
    #'Referer':'http://210.33.28.180/biyesheng/default.aspx',
    #'Accept-Language': 'zh-CN,zh;q=0.8',
    #'Cache-Control':'max-age=0',
    #'Connection':'keep-alive',
    #'Content-Length':317,
    #'Content-Type':'application/x-www-form-urlencoded',
    #'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
}

postData = {
    '__EVENTTARGET' : '',
    '__EVENTARGUMENT' : '',
    '__VIEWSTATE' : '/wEPDwULLTEwNjQ2NTM5MjkPZBYCZg9kFgICAw9kFgYCAg8PFgIeB1Zpc2libGVoZGQCBA8PFgQeCENzc0NsYXNzBQdjdXJyZW50HgRfIVNCAgJkZAIJDxYCHwBoZGSOf2cLF27tMf07H/WFBrfbpg0sVQgWjnH7FjYPM/hSkg==',
    'ctl00$TextBoxXueHao' : '学号',
    'ctl00$TextBoxMiMa' : '密码',
    'ctl00$ButtonDengRu' : '',
}

strpostsata = urllib.urlencode(postData)
req = urllib2.Request(url=baseurl,data=strpostsata)
#html = opener.open(req)
html = urllib2.urlopen(req)
print html.read()
