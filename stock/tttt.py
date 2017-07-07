import pymysql

ff=open("C:\\Users\\xjwhh\\Desktop\\ss\\i.txt",'a')
ff.write("date\topen\thigh\tlow\tclose\tvolume")
ff.write("\n")

db = pymysql.connect("localhost", "root", "123456", "stock", charset="utf8")
cursor = db.cursor()
sql = "select distinct date,adjopen,adjhigh,adjlow,adjclose,volume from kdata_cyb where date>='2016-03-01' and date<='2016-08-01' and code='300001' order by date"
print(sql)
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        date = row[0]
        open = row[1]
        high= row[2]
        low=row[3]
        close=row[4]
        volume=row[5]
        ff.write(str(date)[:10]+"\t")
        ff.write(str(open)+"\t")
        ff.write(str(high)+"\t")
        ff.write(str(low)+"\t")
        ff.write(str(close)+"\t")
        ff.write(str(volume))
        ff.write("\n")
except:
    print('get data fail')

