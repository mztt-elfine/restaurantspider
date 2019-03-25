import requests
from bs4 import BeautifulSoup
import time
from conndb import Mysqlconnect
import hashlib
import re


class Restaurantdata(object):

    def gethtml(self):  # 设置headers，网站会根据这个判断你的浏览器及操作系统，很多网站没有此信息将拒绝你访问
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                          "Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        }
        cookies = {
            "cisession": "19dfd70a27ec0eecf1fe3fc2e48b7f91c7c83c60",
            "CNZZDATA100020196": "1815846425-1478580135-https%253A%252F%252Fwww.baidu.com%252F%7C1483922031",
            "Hm_lvt_f805f7762a9a237a0deac37015e9f6d9": "1482722012,1483926313",
            "Hm_lpvt_f805f7762a9a237a0deac37015e9f6d9": "1483926368"
        }
        for i in range(self.num):
            url = self.url[:-1] + str(i+1)
            # 用get方法打开url并发送headers
            try:
                htm = requests.get(url, headers=headers, cookies=cookies)
            except:
                print("网页数量没这么多！")
            soup = BeautifulSoup(htm.text, "lxml")
            self.parsehtml(soup, self.eny, self.newdb)

    def parsehtml(self, soup, eny, newdb):
        snakedata = soup.select('div[class="listbox"] li.item')
        for i in snakedata:
            eny.update(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())).encode())
            rid = eny.hexdigest()
            sname = i.select(".cn_tit")[0].string
            simage = i.select(".img")[0].get('src')
            pattern = re.compile(r'(^http.+?\.jpg)')
            try:
                simage = pattern.findall(simage)[0]
            except:
                simage = i.select(".img")[0].get('src')

            price = '0'
            addr = 'addr'
            brief = 'brief'
            try:
                price = i.select("dl dd")[0].string[-2:]
                addr = i.select("dl dd")[1].string
                brief = i.select("dl dd")[2].string
            except:
                pass

            if "7dc8cc10cb6b007cc8d65eac.gif" not in simage and price is not "0" and brief is not "brief":
                sql = "insert into restaurants values('{0}','{1}','{2}', '{3}','{4}','{5}', '{6}','{7}')".format(
                    rid, sname, price, addr, brief, simage, time.strftime('%Y/%m/%d', time.localtime(time.time())), "111")
                newdb.dotable(sql)

    def savedb(self):
        try:
            self.newdb = Mysqlconnect()
            self.newdb.create_connect()
            return self.newdb
        except:
            print("don't connect database!")

    def closedb(self):
        self.newdb.closemysql()
        print(" database closed!")
        print("data over!")

    def __init__(self, url, num):
        self.url = url
        self.num = num
        # 加密 id
        self.eny = hashlib.md5()
        self.newdb = None


mywork = Restaurantdata('https://travel.qunar.com/p-cs299897-tonghua-meishi?page=1', 200)
mywork.savedb()
mywork.gethtml()
mywork.closedb()

