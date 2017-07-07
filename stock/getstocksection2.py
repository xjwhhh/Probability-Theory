# coding=utf-8
import urllib.request
from bs4 import BeautifulSoup
import pymysql
#通过股票代码爬取股票名称，证监会行业分类，沪深等板块分类
db=pymysql.connect("localhost", "root", "123456", "stock", use_unicode=True, charset="utf8")
print("fg")
cursor=db.cursor();
# name='恒顺众昇'
# code='300208'
# industry='制造业'
# section='创业板'
# name='索菲亚'
# code='002572'
# industry='制造业'
# section='中小板'
ff=open("C:\\Users\\xjwhh\\Desktop\\newstock2.txt")
f=open("C:\\Users\\xjwhh\\Desktop\\failstock.txt",'a')
list_of_all_the_lines = ff.readlines( )
for i in range(0,len(list_of_all_the_lines)):
    j=list_of_all_the_lines[i]
    j=j[0:6]
    t=j[0:3]
    if(t=="600"):
        section="沪市A股"
    elif (t == "601"):
        section = "沪市A股"
    elif (t == "603"):
        section = "沪市A股"
    elif(t=="900"):
        section="沪市B股"
    elif(t=="000"):
        section="深市A股"
    elif(t=="200"):
        section="深市B股"
    elif(t=="300"):
        section="创业板"
    elif(t=="002"):
        section="中小板"
    else:
        section="无"
    url = "http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpOtherInfo/stockid/"+j+"/menu_num/5.phtml"
    html = urllib.request.urlopen(url)
    bsObj = BeautifulSoup(html, 'lxml')
    aclass = bsObj.select("#stockName")
    aclass1 = bsObj.select(".ct")
    # print(aclass[0].contents[0])
    # print("股票代码：")
    # print(aclass[0].contents[1].contents[0][1:-4])
    # print("所属行业板块：")
    #有板块分类
    if (aclass1[3].contents):
        name = aclass[0].contents[0]#股票名
        code = aclass[0].contents[1].contents[0][1:-4]#股票代码
        industry=aclass1[3].contents[0]#证监会板块
    #无板块分类
    else:
        name= aclass[0].contents[0]
        code= aclass[0].contents[1].contents[0][1:-4]
        industry='无'
    # print(section)
    # print(industry)
    sql = "insert into basicinfo(name,code,industry,section)values('%s','%s','%s','%s')" % (name, code, industry, section)
    try:
        cursor.execute(sql)
        db.commit()
        print(code + " success")
    except:
        db.rollback()
        f.write(code)
        print(code +" fail")
    # cursor.execute(sql)
    # print("我是一条萌萌哒分割线======================================================================")
    # print(" ")
db.close()
