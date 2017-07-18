import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

list=[[1,1,8.12],[1,1,9.25],[1,2,12.8],[1,2,14.2],
      [2,1,22.1],[2,1,16.7],[2,2,30.1],[2,2,23.2]]
df=pd.DataFrame(list,columns=['A','B','result'])
print(df)

formula = 'result~C(A)+C(B)+C(A):C(B)'
anova_results = anova_lm(ols(formula,df).fit())
print (anova_results)