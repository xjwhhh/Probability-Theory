from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5,5,num=150)
y=x**2+np.random.normal(size=x.size)
y[12:14]+=10#增加离群点
y[131:141]-=6
x1=x**2

slope,intercept,r_value,p_value,std_err=stats.linregress(x1,y)

plt.plot(x,y,'b.')
plt.plot(x,slope*x1+intercept,'r-')

print(slope)#斜率
print(intercept)#截距
print(r_value)#r值
print(p_value)#p值
print(std_err)#标准偏差
plt.show()