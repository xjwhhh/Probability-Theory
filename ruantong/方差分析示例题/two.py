from scipy.stats import f
import numpy as np

A1=[27.4,26.7,28.8,33.7,28.8]
A2=[22.8,25.4,28.1,27.6,24.0]
A3=[21.9,23.7,34.9,32.1,26.2]
A4=[32.1,23.7,27.1,26.1,24.5]

A=[A1,A2,A3,A4]
n=20#所有数据量
m=4#因素水平
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

print(F>=f.isf(0.05,m-1,n-m))#上分位数