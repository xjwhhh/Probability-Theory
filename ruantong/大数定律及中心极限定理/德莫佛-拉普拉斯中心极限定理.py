import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

y=[]
n=100
for i in range(1000):
    r=binom.rvs(n,0.3)
    rsum=np.sum(r)
    z=(rsum-n*0.3)/np.sqrt(n*0.3*0.7)
    y.append(z)

plt.hist(y,color='grey')
plt.show()
