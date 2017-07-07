import tushare as ts
import datetime

# df=ts.get_h_data('600001')
# if(df==None):
#     print(1)
# else:
#     print(2)
# print(str(df))
# df=ts.get_stock_basics()
# print(df.ix['601878']['timeToMarket'])

# # df=ts.get_h_data('000001',index=True,start='2017-05-17',end='2017-05-17')
# # print(df)
# date=datetime.datetime.now().strftime('%Y-%m-%d');
# print(date)
# df=ts.get_hist_data('000001',start=date,end=date)
# print(df)
# df=ts.get_hist_data('600087')
# print(df)

# df=ts.get_h_data('000001',start='2004-04-29',end='2004-04-29',autype=None)
# df=ts.get_h_data('000001',start='2014-04-10',end='2014-04-29',autype=None)
# print(df)
#
#
# df=ts.get_h_data('000001',start='2014-04-29',end='2014-04-29')
# print(df)
df=ts.get_stock_basics()
date = df.ix['000001']['timeToMarket']
print(date)
date=str(date)
newdate = date[0:4]+"-"+date[4:6]+"-"+date[6:8]
print(newdate)


