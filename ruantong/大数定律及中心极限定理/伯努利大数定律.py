import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

x=np.arange(1,1001,1)
r=bernoulli.rvs(0.3,size=1000)#p=0.3
y=[]
rsum=0.0
for i in range(1000):
    if(r[i]==1):
        rsum=rsum+1
    y.append(rsum/(i+1))
plt.plot(x,y,color='red')
plt.show()