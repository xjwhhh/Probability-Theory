import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x=np.linspace(-10,10,200)
y=x
X,Y=meshgrid(x,y)
Z=bivariate_normal(X,Y,1,5,0,-5,0)#数字是添加的属性
fig=figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,Z,cmap='OrRd')
plt.show()