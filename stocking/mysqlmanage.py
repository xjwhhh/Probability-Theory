#coding:utf-8
import pymysql
import pandas as pd
# import sys
# import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)

#mysql操作
db=pymysql.connect("localhost","root","123456","stock", charset="utf8")
cursor=db.cursor();

def getstockinfobycode(code):
    sql="select * from basicinfo where code='%s'"%code
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        re=[]
        for row in results:
            name = row[0]
            code = row[1]
            industry = row[2]
            section = row[3]
            resultlist=[name,code,industry,section]
            re.append(resultlist)
        print(re)
        df=pd.DataFrame(re,columns=['name','code','industry','section'])
    except:
        print("get data fail")
    return df

def getkdata_cyb(name,code,startdate,enddate):
    sql="select * from kdata_cyb where code='%s' and date>'%s' and date<'%s'"%(code,startdate,enddate)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        re=[]
        for row in results:
            date = row[0]
            open = row[1]
            high = row[2]
            close = row[3]
            low = row[4]
            volume = row[5]
            amount = row[6]
            # autotype = row[7]
            code=row[8]
            resultlist = [date,open,high,close,low,volume,amount,code]
            re.append(resultlist)
        df=pd.DataFrame(re,columns=['date','open','high','close','low','volumn','amount','code'])
        print(df)
    except:
        print('get data fail')
    return df

