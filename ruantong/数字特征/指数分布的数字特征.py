from scipy.stats import expon
import numpy as np
from scipy import  integrate


rv=expon(scale=2)
print(rv.mean())#数学期望
print(rv.var())#方差
print(rv.moment(1))#k阶矩
print(rv.moment(2))
print(rv.moment(3))
print(rv.moment(4))
print(rv.stats(moments='mvsk'))



#积分计算任意给定概率分布的数字特征，以指数分布为例
E1=lambda x:x*0.5*np.exp(-x/2)
E2=lambda x:x**2*0.5*np.exp(-x/2)
print(integrate.quad(E1,0,np.inf))#0到正无穷
print(integrate.quad(E2,0,np.inf))

print(expon(scale=2).moment(1))
print(expon(scale=2).moment(2))
