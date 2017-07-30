import pandas as pd
import numpy as np
from scipy.stats import f

list = [[1, 1, 12.0], [1, 2, 9.5], [1, 3, 10.4], [1, 4, 9.7], [1, 5, 13.7],
        [2, 1, 11.5], [2, 2, 12.4], [2, 3, 9.6], [2, 4, 14.3], [2, 5, 12.3],
        [3, 1, 11.4], [3, 2, 11.1], [3, 3, 14.2], [3, 4, 14.0], [3, 5, 12.5],
        [4, 1, 12.0], [4, 2, 13.0], [4, 3, 14.0], [4, 4, 13.1], [4, 5, 11.4]]
df = pd.DataFrame(list, columns=['A', 'B', 'result'])

list1 = df['result']
n = 20
a = 4
b = 5
QT = 0
C = 0

#计算各偏差平方和
for i in list1:
    QT = QT + i * i

C = np.sum(list1) * np.sum(list1) / n
ST = QT - C
QA = 0
sum1 = 0
for t in range(0, 4):
    for i in range(5 * t, 5 * (t + 1)):
        sum1 += list1[i]
    QA += sum1 * sum1
    sum1 = 0
QA = QA / b
SA = QA - C
QB = 0
sum2 = 0
for t in range(0, 5):
    for i in [t, t + 5, t + 10, t + 15]:
        sum2 += list1[i]
    QB += sum2 * sum2
    sum2 = 0
QB = QB / a
SB = QB - C
SE = ST - SA - SB

#计算自由度
ft = n - 1
fa = a - 1
fb = b - 1
fe = (a - 1) * (b - 1)

#计算卡方统计量
VA = SA / fa
VB = SB / fb
VE = SE / fe

#计算检验统计量
FA = VA / VE
FB = VB / VE

#查表
f1 = f.isf(0.05, fa, fe)
f2 = f.isf(0.05, fb, fe)

#比较数据得出结论
if (FA < f1):
    print("不同施肥方案对收获量影响不显著")
else:
    print("不同施肥方案对收获量影响显著")
if (FB < f2):
    print("不同种子品种对收获量影响不显著")
else:
    print("不同种子品种对收获量影响显著")


