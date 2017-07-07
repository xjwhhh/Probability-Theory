from scipy import stats

A=[16,18,16,14,12,12]
B=[16,16,16,16,16,8]

print(stats.chisquare(A))#默认均匀分布
print(stats.chisquare(A,f_exp=B))#两者是否来自同一分布