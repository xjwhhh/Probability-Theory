import math
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon as E

def exp(lam):
    p=random.random()#用于生成一个0到1的随机符点数: 0 <= n < 1.0
    return -math.log(1-p)/lam

x1=[]
for i in range(100):
    x1.append(exp(1))
x1=sorted(x1)
y1=np.linspace(0,1,100)
plt.plot(x1,y1,color='blue')

rv=E(scale=1)
x2=np.linspace(0,5,100)
plt.plot(x2,rv.cdf(x2),color='red')
plt.show()