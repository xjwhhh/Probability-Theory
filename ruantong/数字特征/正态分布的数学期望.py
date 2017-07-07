from scipy.stats import norm

f1=lambda x:x**4
f2=lambda x:x**2-x+2

print(norm.expect(f1,loc=1,scale=2))
print(norm.expect(f2,loc=1,scale=5))