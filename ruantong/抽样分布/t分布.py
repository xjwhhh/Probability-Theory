import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import *

fig,ax=plt.subplots(1,1)
df=10#自由度
x=np.linspace(-4,4,100)
ax.plot(x,t.pdf(x,df))

y=[]
for i in range(1000):
    rx=norm.rvs()
    ry=chi2.rvs(df)
    rt=rx/np.sqrt(ry/df)
    y.append(rt)
ax.hist(y,normed=True,alpha=0.2)
plt.show()