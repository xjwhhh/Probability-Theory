from scipy.stats import uniform

rv=uniform(loc=2,scale=6)#a=2,b=2+6
print(rv.mean())#数学期望
print(rv.var())#方差
print(rv.moment(1))#k阶矩
print(rv.moment(2))
print(rv.moment(3))
print(rv.moment(4))
print(rv.stats(moments='mvsk'))