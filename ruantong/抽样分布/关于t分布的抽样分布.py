import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import *

fig,ax=plt.subplots(1,1)
df=10
x=np.linspace(t.ppf(0.01,df),t.ppf(0.99,df),100)
ax.plot(x,t.pdf(x,df))

y=[]
for i in range(1000):
    r=norm.rvs(loc=5,scale=2,size=df+1)
    rt=(np.mean(r)-5)/np.sqrt(np.var(r)/df)
    y.append(rt)
ax.hist(y,normed=True,alpha=0.2)
plt.show()