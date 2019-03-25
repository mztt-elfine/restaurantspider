import pymysql


class Mysqlconnect(object):
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.password = 'root5454'
        self.db = 'camdata'
        self.table = 'restaurants'

    def create_connect(self):
            try:
                self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db, charset='utf8')
                self.cursor = self.conn.cursor()
            except:
                print("can't connect mysql!")

    # 去重
    def checkdata(self, str):
        sqlfield = "select url from restaurants where url='%s'".format(str)
        if self.cursor.execute(sqlfield):
            return True
        else:
            return False

    # 操作表
    def dotable(self, sql):

        try:
            self.cursor.execute(sql)
            # 插入提交
            self.conn.commit()
            # 查询
            # row = self.cursor.fetchone()
        except:
            print("nothing!")

    def closemysql(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    print("这里执行了。。。")
