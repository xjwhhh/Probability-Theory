from scipy import stats
from scipy.stats import f
import numpy as np

A1=[27.0,26.2,28.8,33.5,28.8]
A2=[22.8,23.1,27.7,27.6,24.0]
A3=[21.9,23.4,20.1,27.8,19.3]
A4=[23.5,19.6,23.7,20.8,23.9]

print(stats.f_oneway(A1,A2,A3,A4))

m=4#因素水平
n=20#所有数据数量
print(f.sf(6.4231,m-1,n-m))#由F值得p值

print(f.isf(0.05,m-1,n-m))#上分位数
print(f.isf(0.01,m-1,n-m))



A=[A1,A2,A3,A4]
n=20
As=np.sum(A,axis=1)#行和
QA=0.0#水平间数据平方和
for i in range(4):
    QA=QA+As[i]*As[i]
QA=QA/5
QT=0.03#总数据平方和
for i in range(4):
    for j in range(5):
        QT=QT+A[i][j]*A[i][j]
C=np.sum(A)*np.sum(A)/n#修正项
ST=QT-C#总偏差平方和
SA=QA-C#水平间偏差平方和
Se=ST-SA#水平内偏差平方和
F=(SA/3)/(Se/16)
