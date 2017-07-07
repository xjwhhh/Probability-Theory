from sqlalchemy import create_engine
import tushare as ts

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1/stock?charset=utf8')
#获取大盘数据近三年平均数据
startdate='2017-05-18'
enddate='2017-05-19'
#上证指数
df=ts.get_hist_data('sh',start=startdate,end=enddate)
df= df.iloc[:, 5:]#去除开盘收盘最高最低成交量数据
df['code']="上证指数"
df.to_sql('average_data', engine, if_exists='append')


#深圳成指
df=ts.get_hist_data('sz',start=startdate,end=enddate)
df= df.iloc[:, 5:]#去除开盘收盘最高最低成交量数据
df['code']="深圳成指"
df.to_sql('average_data', engine, if_exists='append')


#沪深300
df=ts.get_hist_data('hs300',start=startdate,end=enddate)
df= df.iloc[:, 5:]#去除开盘收盘最高最低成交量数据
df['code']="沪深300"
df.to_sql('average_data', engine, if_exists='append')


#上证50
df=ts.get_hist_data('sz50',start=startdate,end=enddate)
df= df.iloc[:, 5:]#去除开盘收盘最高最低成交量数据
df['code']="上证50"
df.to_sql('average_data', engine, if_exists='append')


#中小板
df=ts.get_hist_data('zxb',start=startdate,end=enddate)
df= df.iloc[:, 5:]#去除开盘收盘最高最低成交量数据
df['code']="中小板"
df.to_sql('average_data', engine, if_exists='append')

#创业板
df=ts.get_hist_data('cyb',start=startdate,end=enddate)
df= df.iloc[:, 5:]#去除开盘收盘最高最低成交量数据
df['code']="创业板"
df.to_sql('average_data', engine, if_exists='append')
