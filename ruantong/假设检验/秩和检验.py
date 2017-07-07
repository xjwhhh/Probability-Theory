from scipy import stats

a=stats.norm.rvs(size=20)
b=stats.norm.rvs(size=20)
c=stats.expon.rvs(size=20)

print(stats.ranksums(a,b))
print(stats.ranksums(b,c))
