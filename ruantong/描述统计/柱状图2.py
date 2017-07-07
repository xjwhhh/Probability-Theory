import numpy as np
import matplotlib.pyplot as plt

menMeans=(20,35,30,35,27)
menStd=(2,3,4,1,2)
womenMeans=(25,32,34,20,25)
womenStd=(3,5,2,3,3)

ind=np.arange(5)
width=0.35
fig,ax=plt.subplots()
rects1=ax.bar(ind,menMeans,width,color='r',yerr=menStd)
rects2=ax.bar(ind+width,womenMeans,width,color='y',yerr=womenStd)

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind+width)
ax.set_xticklabels(('G1,''G2','G3','G4','G5'))#有问题
ax.legend((rects1[0],rects2[0]),('Men','Women'))
plt.show()