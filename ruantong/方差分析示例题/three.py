import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm


# list=[[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,],
#       [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],
#       [12.0,9.5,10.4,9.7,13.7,11.5,12.4,9.6,14.3,12.3,11.4,11.1,14.2,14,0,12.5,12.0,13.0,14.0,13.1,11.4]]
list=[[1,1,12.0],[1,2,9.5],[1,3,10.4],[1,4,9.7],[1,5,13.7],
      [2,1,11.5],[2,2,12.4],[2,3,9.6],[2,4,14.3],[2,5,12.3],
      [3,1,11.4],[3,2,11.1],[3,3,14.2],[3,4,14.0],[3,5,12.5],
      [4,1,12.0],[4,2,13.0],[4,3,14.0],[4,4,13.1],[4,5,11.4]]
df=pd.DataFrame(list,columns=['A','B','result'])
print(df)

formula = 'result~C(A)+C(B)+C(A):C(B)'
anova_results = anova_lm(ols(formula,df).fit())
print (anova_results)


