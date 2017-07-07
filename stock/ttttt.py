import tushare as ts
import pymysql

df=ts.get_h_data('000001','2017-06-12','2017-06-12')
print(df)
# df=ts.get_today_all()
# print(df)

# ff=open("C:\\Users\\xjwhh\\Desktop\\aaa.txt",'a')
#
# def getStocks():
#     sql = "select distinct code from basicinfo"
#     try:
#         cursor.execute(sql)
#         results = cursor.fetchall()
#         re = []
#         for row in results:
#             re.append(row[0])
#             ff.write(str(row[0]))
#             ff.write('\n')
#     except:
#         print('get data fail')
#     return re
#
#
# db = pymysql.connect("localhost", "root", "123456", "stock", charset="utf8")
# cursor = db.cursor()
# getStocks()