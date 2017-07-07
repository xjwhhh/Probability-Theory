from sqlalchemy import create_engine
import tushare as ts
import datetime
#获取大盘指数开盘以来所有k线数据
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1/stock?charset=utf8')

# startdate=datetime.datetime.now().strftime('%Y-%m-%d');
# enddate=datetime.datetime.now().strftime('%Y-%m-%d');
startdate='2017-06-06'
enddate='2017-06-09'
#上证指数
# df=ts.get_h_data('000001',index=True,start='1991-07-15',end='2017-05-15')
# df=ts.get_h_data('000001',index=True,start='2017-05-16',end='2017-05-17')
df=ts.get_h_data('000001',index=True,start=startdate,end=enddate)
df['code']='上证指数'
df.to_sql('market_index', engine, if_exists='append')

# df=ts.get_h_data('000001',index=True,start='1991-07-15',end='2017-05-15',autype='hfq')
# df=ts.get_h_data('000001',index=True,start='2017-05-16',end='2017-05-17',autype='hfq')
# df=ts.get_h_data('000001',index=True,start=startdate,end=enddate,autype='hfq')
# df['autotype']='后复权'
# df['code']='上证指数'
# df.to_sql('market_index', engine, if_exists='append')

# df=ts.get_h_data('000001',index=True,start='1991-07-15',end='2017-05-15',autype=None)
# df=ts.get_h_data('000001',index=True,start='2017-05-16',end='2017-05-17',autype=None)
# df=ts.get_h_data('000001',index=True,start=startdate,end=enddate,autype=None)
# df['autotype']='无复权'
# df['code']='上证指数'
# df.to_sql('market_index', engine, if_exists='append')

#深圳成指
# df=ts.get_h_data('399001',index=True,start='1991-04-03',end='2017-05-15')
# df=ts.get_h_data('399001',index=True,start='2017-05-16',end='2017-05-17')
df=ts.get_h_data('399001',index=True,start=startdate,end=enddate)
df['code']='深圳成指'
df.to_sql('market_index', engine, if_exists='append')

# # df=ts.get_h_data('399001',index=True,start='1991-04-03',end='2017-05-15',autype='hfq')
# # df=ts.get_h_data('399001',index=True,start='2017-05-16',end='2017-05-17',autype='hfq')
# df=ts.get_h_data('399001',index=True,start=startdate,end=enddate,autype='hfq')
# df['autotype']='后复权'
# df['code']='深圳成指'
# df.to_sql('market_index', engine, if_exists='append')
#
# # df=ts.get_h_data('399001',index=True,start='1991-04-03',end='2017-05-15',autype=None)
# # df=ts.get_h_data('399001',index=True,start='2017-05-16',end='2017-05-17',autype=None)
# df=ts.get_h_data('399001',index=True,start=startdate,end=enddate,autype=None)
# df['autotype']='无复权'
# df['code']='深圳成指'
# df.to_sql('market_index', engine, if_exists='append')

#沪深300
# df=ts.get_h_data('000300',index=True,start='2005-04-08',end='2017-05-15')
# df=ts.get_h_data('000300',index=True,start='2017-05-16',end='2017-05-17')
df=ts.get_h_data('000300',index=True,start=startdate,end=enddate)
df['code']='沪深300'
df.to_sql('market_index', engine, if_exists='append')

# df=ts.get_h_data('000300',index=True,start='2005-04-08',end='2017-05-15',autype='hfq')
# df=ts.get_h_data('000300',index=True,start='2017-05-16',end='2017-05-17',autype='hfq')
# df=ts.get_h_data('000300',index=True,start=startdate,end=enddate,autype='hfq')
# df['autotype']='后复权'
# df['code']='沪深300'
# df.to_sql('market_index', engine, if_exists='append')
#
# # df=ts.get_h_data('000300',index=True,start='2005-04-08',end='2017-05-15',autype=None)
# # df=ts.get_h_data('000300',index=True,start='2017-05-16',end='2017-05-17',autype=None)
# df=ts.get_h_data('000300',index=True,start=startdate,end=enddate,autype=None)
# df['autotype']='无复权'
# df['code']='沪深300'
# df.to_sql('market_index', engine, if_exists='append')

#上证50
# df=ts.get_h_data('000016',index=True,start='2004-01-02',end='2017-05-15')
# df=ts.get_h_data('000016',index=True,start='2017-05-16',end='2017-05-17')
df=ts.get_h_data('000016',index=True,start=startdate,end=enddate)
df['code']='上证50'
df.to_sql('market_index', engine, if_exists='append')

# # df=ts.get_h_data('000016',index=True,start='2004-01-02',end='2017-05-15',autype='hfq')
# # df=ts.get_h_data('000016',index=True,start='2017-05-16',end='2017-05-17',autype='hfq')
# df=ts.get_h_data('000016',index=True,start=startdate,end=enddate,autype='hfq')
# df['autotype']='后复权'
# df['code']='上证50'
# df.to_sql('market_index', engine, if_exists='append')
#
# # df=ts.get_h_data('000016',index=True,start='2004-01-02',end='2017-05-15',autype=None)
# # df=ts.get_h_data('000016',index=True,start='2017-05-16',end='2017-05-17',autype=None)
# df=ts.get_h_data('000016',index=True,start=startdate,end=enddate,autype=None)
# df['autotype']='无复权'
# df['code']='上证50'
# df.to_sql('market_index', engine, if_exists='append')

#中小板
# df=ts.get_h_data('399005',index=True,start='2004-06-25',end='2017-05-15')
# df=ts.get_h_data('399005',index=True,start='2017-05-16',end='2017-05-17')
df=ts.get_h_data('399005',index=True,start=startdate,end=enddate)
df['code']='中小板'
df.to_sql('market_index', engine, if_exists='append')

# # df=ts.get_h_data('399005',index=True,start='2004-06-25',end='2017-05-15',autype='hfq')
# # df=ts.get_h_data('399005',index=True,start='2017-05-16',end='2017-05-17',autype='hfq')
# df=ts.get_h_data('399005',index=True,start=startdate,end=enddate,autype='hfq')
# df['autotype']='后复权'
# df['code']='中小板'
# df.to_sql('market_index', engine, if_exists='append')
#
# # df=ts.get_h_data('399005',index=True,start='2004-06-25',end='2017-05-15',autype=None)
# # df=ts.get_h_data('399005',index=True,start='2017-05-16',end='2017-05-17',autype=None)
# df=ts.get_h_data('399005',index=True,start=startdate,end=enddate,autype=None)
# df['autotype']='无复权'
# df['code']='中小板'
# df.to_sql('market_index', engine, if_exists='append')

#创业板
# df=ts.get_h_data('399006',index=True,start='2009-10-30',end='2017-05-15')
# df=ts.get_h_data('399006',index=True,start='2017-05-16',end='2017-05-17')
df=ts.get_h_data('399006',index=True,start=startdate,end=enddate)
df['code']='创业板'
df.to_sql('market_index', engine, if_exists='append')

# # df=ts.get_h_data('399006',index=True,start='2009-10-30',end='2017-05-15',autype='hfq')
# # df=ts.get_h_data('399006',index=True,start='2017-05-16',end='2017-05-17',autype='hfq')
# df=ts.get_h_data('399006',index=True,start=startdate,end=enddate,autype='hfq')
# df['autotype']='后复权'
# df['code']='创业板'
# df.to_sql('market_index', engine, if_exists='append')
#
# # df=ts.get_h_data('399006',index=True,start='2009-10-30',end='2017-05-15',autype=None)
# # df=ts.get_h_data('399006',index=True,start='2017-05-16',end='2017-05-17',autype=None)
# df=ts.get_h_data('399006',index=True,start=startdate,end=enddate,autype=None)
# df['autotype']='无复权'
# df['code']='创业板'
# df.to_sql('market_index', engine, if_exists='append')

