from scipy import stats
from scipy.stats import f

A1=[27.4,26.7,28.8,33.7,28.8]
A2=[22.8,25.4,28.1,27.6,24.0]
A3=[21.9,23.7,34.9,32.1,26.2]
A4=[32.1,23.7,27.1,26.1,24.5]

result=stats.f_oneway(A1,A2,A3,A4)
# print(result[0])#F
# print(result[1])#p-value

m=4#因素水平
n=20#所有数据数量
# print(f.sf(result[0],m-1,n-m))#由F值得p值

# print(f.isf(0.05,m-1,n-m))#0.05上分位数
# print(f.isf(0.01,m-1,n-m))#0.01上分位数

if(result[0]>=f.isf(0.05,m-1,n-m)):
    print("这四种除杂方法有显著差别")
else:
    print("这四种除杂方法没有显著差别")
