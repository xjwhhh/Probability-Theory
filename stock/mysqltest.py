#coding:utf-8
import pymysql
#创建表格并手动填充一些数据
db=pymysql.connect("localhost","root","123456","stock", charset="utf8")
# db.set_charset('utf-8')

print("fg")
cursor=db.cursor();
# name1='恒顺众昇'
# code1='300208'
# industry1='制造业'
# section1='创业板'
name1='舜喆B'
code1='200168'
industry1='房地产开发与经营业'
section1='深市B股'
# name1='昇兴股份'
# code1='002752'
# industry1='制造业'
# section1='中小板'
# sql = "insert into basicinfo(name,code,industry,section)values('%s','%s','%s','%s')"%(name1,code1,industry1,section1)
# sql="create table basicinfo(name varchar(20) not null,code char(6) not null,industry varchar(30) not null,section varchar(255) not null)"
sql="create table clientinfo(id integer not null,name varchar(255) not null,password varchar(255) not null)"
cursor.execute(sql)
db.commit()
cursor.close()
print("success")
# result=cursor.fetchall()
# for rows in result:
#     print(rows)