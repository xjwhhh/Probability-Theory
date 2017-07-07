import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import *

fig,ax=plt.subplots(1,1)
x=np.linspace(-4,4,100)
ax.plot(x,norm.pdf(x))

#关于指数分布的抽样分布
y=[]
n=100
for i in range(1000):
    r=expon.rvs(scale=1,size=n)
    rsum=np.sum(r)
    z=(rsum-n)/np.sqrt(n)
    y.append(z)
ax.hist(y,normed=True,alpha=0.2)
plt.show()


#正态分布
# y=[]
# n=100
# for i in range(1000):
#     r=norm.rvs(loc=5,scale=2,size=n)
#     rsum=np.sum(r)
#     z=(rsum-n*5)/np.sqrt(n*4)
#     y.append(z)
# ax.hist(y,normed=True,alpha=0.2)
# plt.show()