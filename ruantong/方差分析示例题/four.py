import pandas as pd
import numpy as np
from scipy.stats import f

list=[[1,1,8.12],[1,1,9.25],[1,1,11.31],[1,2,12.8],[1,2,14.2],[1,2,13.1],
      [2,1,22.1],[2,1,16.7],[2,1,18.2],[2,2,30.1],[2,2,23.2],[2,2,25.53]]
df=pd.DataFrame(list,columns=['A','B','result'])
print(df)

list1 = df['result']
n = 12
a = 2
b = 2
r=3
QT = 0
C = 0

#计算各偏差平方和
for i in list1:
    QT = QT + i * i

C = np.sum(list1) * np.sum(list1) / n
ST = QT - C
QA = 0
sum1 = 0
for t in range(0, 2):
    for i in range(6 * t, 6 * (t + 1)):
        sum1 += list1[i]
    QA += sum1 * sum1
    sum1 = 0
QA = QA / (b*r)
SA = QA - C
QB = 0
sum2 = 0
for t in [0,3]:
    for i in [t, t + 1,  t+2,t+6,t+7,t+8]:
        sum2 += list1[i]
    QB += sum2 * sum2
    sum2 = 0
QB = QB / (a*r)
SB = QB - C
QAB=0
sum3=0
for i in range(0,4):
    for j in [3*i,3*i+1,3*i+2]:
        sum3+=list1[j]
    QAB+=sum3*sum3
    sum3=0
QAB=QAB/r
SAB=QAB-QA-QB+C
SE=QT-QAB

#计算自由度
ft=n-1
fa=a-1
fb=b-1
fab=(a-1)*(b-1)
fe=a*b*(r-1)

#计算卡方统计量
VA=SA/fa
VB=SB/fb
VAB=SAB/fab
VE=SE/fe

#计算检验统计量
FA=VA/VE
FB=VB/VE
FAB=VAB/VE

#查表
f1 = f.isf(0.05, fa, fe)
f2 = f.isf(0.05, fb, fe)
f3 = f.isf(0.05, fab, fe)

#比较数据得出结论
if (FA < f1):
    print("不同广告方案对销售量影响不显著")
else:
    print("不同广告方案对销售量影响显著")
if (FB < f2):
    print("不同广告媒体对销售量影响不显著")
else:
    print("不同广告媒体对销售量影响显著")
if(FAB<f3):
    print("不同广告方案和广告媒体交互作用对销售量影响不显著")
else:
    print("不同广告方案和广告媒体交互作用对销售量影响显著")










