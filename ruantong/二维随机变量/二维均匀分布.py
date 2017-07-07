import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
ax=fig.gca(projection='3d')
X=np.arange(0,1,0.01)
Y=np.arange(0,1,0.01)
X,Y=np.meshgrid(X,Y)#100*100的区域
Z1=1
Z2=0
surf=ax.plot_surface(X,Y,Z1,color='b')
surf=ax.plot_surface(X,Y,Z2,color='r')#表面渲染

plt.show()