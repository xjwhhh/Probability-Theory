import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon as E

rv1=E(scale=1.5)
rv2=E(scale=1.0)
rv4=E(scale=1.0)
rv3=E(scale=0.5)

x=np.linspace(0,20,100)
plt.plot(x,rv1.pdf(x),color='green')
plt.plot(x,rv2.pdf(x),color='blue')
plt.plot(x,rv3.pdf(x),color='red')
plt.plot(x,rv3.cdf(x),color='red')#pdf(x)+cdf(x)=1


plt.show()