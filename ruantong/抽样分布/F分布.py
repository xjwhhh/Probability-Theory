import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import *

fig,ax=plt.subplots(1,1)
dfn,dfm=10,5
x=np.linspace(f.ppf(0.01,dfn,dfm),f.ppf(0.99,dfn,dfm),100)
ax.plot(x,f.pdf(x,dfn,dfm))

y=[]
for i in range(1000):
    rx=chi2.rvs(dfn)
    ry=chi2.rvs(dfm)
    rf=np.sqrt(rx/dfn)/np.sqrt(ry/dfm)
    y.append(rf)
ax.hist(y,normed=True,alpha=0.2)
plt.show()