from sqlalchemy import create_engine
import tushare as ts
import datetime

f=open("C:\\Users\\xjwhh\\Desktop\\failstock.txt",'a')

# startdate=datetime.datetime.now().strftime('%Y-%m-%d');
# enddate=datetime.datetime.now().strftime('%Y-%m-%d');
startdate='2017-05-18'
enddate='2017-05-19'
#获取股票近三年平均数据数据
def get_hist_data_dayk(i):
    df=ts.get_hist_data(i,start=startdate,end=enddate)
    if(str(df)=="None"):
        print(i+"fail")
        f.write(i)
        f.write("\n")
    else:
        print(i)
        df= df.iloc[:, 5:]#去除开盘收盘最高最低成交量数据
        df['code']=i
        # df['ktype']='day'
        # print(df)
        df.to_sql('average_data', engine, if_exists='append')

# #获取股票近三年周K线数据
# def get_hist_data_weekk(i):
#     df = ts.get_hist_data(i,ktype='W')
#     df['code'] = i
#     df['ktype'] = 'week'
#     # print(df)
#     df.to_sql('weekk_data', engine, if_exists='append')
#
# #获取股票近三年月K线数据
# def get_hist_data_monthk(i):
#     df = ts.get_hist_data(i,ktype='M')
#     df['code'] = i
#     df['ktype'] = 'month'
#     # print(df)
#     df.to_sql('monthk_data', engine, if_exists='append')

#获取股票一段时间内的前复权数据
def get_h_data_qfq(i,starttime,endtime):
    df=ts.get_h_data(i,start=starttime,end=endtime)
    df['code']=i
    df['autype']='前复权'
    # print(df)
    df.to_sql('qfq_data', engine, if_exists='append')

#获取股票一段时间内的后复权数据
def get_h_data_qfq(i,starttime,endtime):
    df=ts.get_h_data(i,start=starttime,end=endtime,autype='hfq')
    df['code']=i
    df['autype']='后复权'
    # print(df)
    df.to_sql('hfq_data', engine, if_exists='append')

#获取股票某天的历史分笔数据
def get_tick_data(i,date):
    df=ts.get_tick_data(i,date=date)
    df['date']=date
    df['code']=i
    # print(df)
    df.to_sql('tick_data', engine, if_exists='append')

# stock_basics_info=ts.get_stock_basics()
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1/stock?charset=utf8')
# get_hist_data_dayk('000001')

ff=open("C:\\Users\\xjwhh\\Desktop\\newstock1.txt")
list_of_all_the_lines = ff.readlines( )
for i in range(0,len(list_of_all_the_lines)):
    j=list_of_all_the_lines[i]
    # print(j.type())
# t=0
# for i in stock_basics_info.index:
    # print(i)
    # date = stock_basics_info.ix[i]['timeToMarket']
    # print(date)'
    j=j[0:6]
    # print(j)
    # ff.write(i)
    # ff.write('\n')
    get_hist_data_dayk(j)
    # t=t+1
    # print(t)
    # get_hist_data_weekk(i)
    # print(2)
    # get_hist_data_monthk(i)
    # print(3)
    # print("success")






