# coding=utf-8

import requests
import re


url = 'https://www.woyaogexing.com/touxiang/z/nvxqx/'

# 设置headers，网站会根据这个判断你的浏览器及操作系统，很多网站没有此信息将拒绝你访问
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                 " Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36"}

# 用get方法打开url并发送headers

html = requests.get(url, headers=header)
res = html.text

pattern = re.compile(r'((?<= src=").+\.jpeg">)')
# pattern = re.compile(r'(^https:.+?\.jpg)')

lst = pattern.findall(res)
for i in lst:
    print("https:{0}".format(i))



