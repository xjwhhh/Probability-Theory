import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import *

fig,ax=plt.subplots(1,1)
df=10#自由度
x=np.linspace(chi2.ppf(0.01,df),chi2.ppf(0.99,df),100)
ax.plot(x,chi2.pdf(x,df))

y=[]
n=10#自由度
for i in range(1000):
    chi2r=0.0
    r=norm.rvs(size=n)
    for j in range(n):
        chi2r=chi2r+r[j]**2
    y.append(chi2r)
ax.hist(y,normed=True,alpha=0.2)
plt.show()