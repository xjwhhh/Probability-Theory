import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm as N

x=np.linspace(-10,10,100)#创建等差数列，开始，结束，个数
rv1=N(loc=0,scale=1)#loc=u,sclae=o
rv2=N(loc=-5,scale=1)
rv3=N(loc=0,scale=3)

plt.plot(x,rv1.pdf(x),color='green')
plt.plot(x,rv2.pdf(x),color='blue')
plt.plot(x,rv3.pdf(x),color='red')
plt.show()