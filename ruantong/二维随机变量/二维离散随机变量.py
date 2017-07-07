from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

#x=1,不吸烟，x=2吸烟一般，x=3吸烟严重
#y=-1,不健康，y=0普通，y=1健康

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
dx=0.3
dy=0.3
dz=[0.02,0.025,0.35,0.1,0.15,0.04,0.25,0.04,0.025]#柱子的长宽高
zpos=0
i=0
for xpos in [1,2,3]:
    for c,ypos in zip(['r','y','g'],[-1,0,1]):
        ax.bar3d(xpos,ypos,zpos,dx,dy,dz[i],color=c)
        i=i+1
plt.show()