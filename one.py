import time
import hashlib
import re
import conndb
# eny = hashlib.md5()
# tt = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())).encode()
# # tt = time.time().encode()
# eny.update(tt)
# print(eny.hexdigest())
newdd = conndb.create_connect()
str = "¥ 43"
print(str[-2:])
# pattern = re.compile(r'(^https:.+?\.jpg)')
# image = pattern.findall(str)
# print(pattern.findall(str)[0])
# res = html.text
# soup = BeautifulSoup(html, "lxml")
# div_list = soup.find_all('div', class_='snack_list_con')

# print(div_list)

# pattern = re.compile(r'((?<= src=").+\.jpg)')
# lst = pattern.findall(res)
# for i in lst:
#     print("https:{0}".format(i))

url = 'https://travel.qunar.com/p-cs299897-tonghua-meishi?page=1'
# for i in range(10):
#     url = url[0:-1] + str(i+1)
#     print(url)
