import numpy as np
import matplotlib.pyplot as plt

inc=0.1
e1=np.random.normal(0,1,size=(500,))
e2=np.random.normal(0,1,size=(500,))
e3=np.random.normal(0,1+inc,size=(500,))
e4=np.random.normal(0,1+2*inc,size=(500,))

treatments=[e1,e2,e3,e4]

plt.boxplot(treatments)
plt.show()