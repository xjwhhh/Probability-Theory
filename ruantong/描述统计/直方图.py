import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sta

X=sta.norm(loc=950,scale=20)
plt.hist(X.rvs(size=100),color='yellowgreen')
plt.show()