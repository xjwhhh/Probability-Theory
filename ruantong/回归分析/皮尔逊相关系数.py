from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-5,5,num=150)
y=x+np.random.normal(size=x.size)
y[12:14]+=10#增加离群点

print(stats.pearsonr(x,y))
plt.scatter(x,y)
plt.show()