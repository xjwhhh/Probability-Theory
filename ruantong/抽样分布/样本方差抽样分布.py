import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import *

fig,ax=plt.subplots(1,1)
df=10#自由度
x=np.linspace(chi2.ppf(0.01,df),chi2.ppf(0.99,df),100)
ax.plot(x,chi2.pdf(x,df))

y=[]
for i in range(1000):
    r=norm.rvs(loc=5,scale=2,size=df+1)
    rchi2=df*np.var(r)/4
    y.append(rchi2)
ax.hist(y,normed=True,alpha=0.2)
plt.show()