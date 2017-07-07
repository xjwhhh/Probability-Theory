import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import *

fig,ax=plt.subplots(1,1)
dfn,dfm=10,5
x=np.linspace(f.ppf(0.01,dfn,dfm),f.ppf(0.99,dfn,dfm),100)
ax.plot(x,f.pdf(x,dfn,dfm))

y=[]
for i in range(1000):
    r1=norm.rvs(loc=5,scale=2,size=dfn+1)
    r2=norm.rvs(loc=3,scale=2,size=dfm+1)
    rf=np.var(r1)/np.var(r2)
    y.append(rf)
ax.hist(y,normed=True,alpha=0.2)
plt.show()
