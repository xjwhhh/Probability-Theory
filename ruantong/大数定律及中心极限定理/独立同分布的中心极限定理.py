import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

y=[]
n=100
for i in range(1000):
    r=expon.rvs(scale=1,size=n)
    rsum=np.sum(r)
    z=(rsum-n)/np.sqrt(n)
    y.append(z)

plt.hist(y,color='grey')
plt.show()