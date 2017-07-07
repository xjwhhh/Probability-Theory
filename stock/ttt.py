# import pymysql
# import tushare as ts

# db=pymysql.connect("localhost","root","123456","stock", charset="utf8")
# cursor=db.cursor();
#
# sql="select code,industry from basicinfo "
# cursor.execute(sql)
# results = cursor.fetchall()
# for row in results:
#     code=row[0]
#     industry=row[1]
#     f = open("C:\\Users\\xjwhh\\Desktop\\stock\\行业分类\\" + industry + ".txt", 'a')
#     f.write(code)
#     f.write("\n")
# startdate='2017-06-04'
# enddate='2017-06-04'
#
# newdf = ts.get_h_data('000001', start=startdate, end=enddate)
# newdf2 = ts.get_h_data('000001', start=startdate, end=enddate, autype=None)
# if (str(newdf) != 'None'):
#     newdf3 = newdf.iloc[:, 0:4];
#     newdf3.rename(columns={'close': "adjclose", 'open': 'adjopen', 'high': 'adjhigh', 'low': 'adjlow'}, inplace=True)
#     d = newdf2.join(newdf3)
#     print(d)
# else:
#     print(2345)

import pymysql
import pandas as pd


class Cache(object):
    def __init__(self, ):
        self.data = []

    def getStockInfo(self, code, section, startDate, endDate):
        db = pymysql.connect("localhost", "root", "123456", "stock", charset="utf8")
        cursor = db.cursor()
        sql = "select distinct date,adjclose from kdata_" + section + " where date>='%s' and date<='%s' and code='%s' order by date" % (
            startDate, endDate, code)
        print(sql)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            re = []
            for row in results:
                date = row[0]
                close = row[1]
                resultlist = [date, close]
                re.append(resultlist)
        except:
            print('get data fail')
        return re



cache = Cache()
tt=cache.getStockInfo('000001','sza','2017-05-12','2017-06-01')
print(tt)
