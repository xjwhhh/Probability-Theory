import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom as G

rv=G(0.2)#p=0.2
x=np.arange(1,11,1)
y=rv.pmf(x)

plt.bar(x,y,width=0.6,color='grey')
plt.show()
print(y)