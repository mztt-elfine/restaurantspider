import requests
from bs4 import BeautifulSoup
import pymysql
import re


# 解析链接
def parse(url):
    html = requests.get(url)
    html = html.text
    soup = BeautifulSoup(html, 'lxml')
    # 找到li标签，该标签内有两个class属性，分别为book,clearfix
    data = soup.find_all('li', {'class': {'book', 'clearfix'}})
    # 解析该data
    for i in data:
        name = i.h3.a.text
        zz_fl = i.p.text
        # 将得到的数据按|来拆分，拆分后为一个列表，其中有两个元素，但元素中有空格
        # 所以要使用strip来去除空格
        zz_fl = zz_fl.split('|')
        zuoze = zz_fl[0].strip()
        fenlei = zz_fl[1].strip()
        print('书名：{0}  作者：{1}  类别：{2}'.format(name, zuoze, fenlei))
        # 将得到的数据传送给MySQL
        mysql(name, zuoze, fenlei)
    # 解析完后再进行下一步解析
    next_page(url)


# 查找下一页url
def next_page(nextpage):
    # 将得到的下一页的url由自己指定
    # 匹配http://www.jingyu.com/search/stack?pn=1后面的数字
    a = re.search('pn=(.*)', nextpage).group(1)
    # 匹配http://www.jingyu.com/search/stack?pn=1数字前面的值
    # 这里我不用字符串的split('=')，主要为了练习正则
    start_url = re.findall('.*pn=', nextpage)[0]
    a = int(a)
    # 总共25页，只需要爬取25页就可以
    if a <= 25:
        a += 1
        nextpage = start_url + str(a)
        if a <= 25:
            # 只要url还未到25页，那么就继续解析
            parse(nextpage)
        else:
            print('结束翻页')


# 定义一个类，将连接MySQL的操作写入其中
class down_mysql:
    def __init__(self, name, zuoze, fenlei):
        self.name = name
        self.zuoze = zuoze
        self.fenlei = fenlei
        self.connect = pymysql.connect(
            host='localhost',
            db='test',
            port=3306,
            user='root',
            passwd='123456',
            charset='utf8',
            use_unicode=False
        )
        self.cursor = self.connect.cursor()

    # 保存数据到MySQL中
    def save_mysql(self):
        sql = "insert into xs(`name`,zuoze,fenlei) VALUES (%s,%s,%s)"
        try:
            self.cursor.execute(sql, (self.name, self.zuoze, self.fenlei))
            self.connect.commit()
            print('数据插入成功')
        except:
            print('数据插入错误')


# 新建对象，然后将数据传入类中
def mysql(name, zuoze, fenlei):
    down = down_mysql(name, zuoze, fenlei)
    down.save_mysql()


if __name__ == '__main__':
    # 给定一个初始的url
    url = 'http://www.jingyu.com/search/stack?pn=1'
    # 解析该url
    parse(url)
