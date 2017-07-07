'''
利用python实现简化版描述函数

注意事项：

1）不能调用math、scipy、numpy包

2）为了使正态分布峰度为0，此处对峰度值做减3处理

3）当输入数据仅包含一个元素时，方差返回None

[mean,var,skew,kurt]分别代表均值、方差、偏度、峰度
'''
import numpy as np
#
# class Solution():
#     def solve(self,a):
#         if len(a)==1:
#             return None
#         sum=0
#         for i in a:
#             sum=sum+i
#         mean=sum/len(a)
#
#         sum2=0
#         sum13=0
#         sum14=0
#         for i in a:
#             sum2=sum2+(i-mean)**2
#             sum13=sum13+(i-mean)**3
#             sum14=sum14+(i-mean)**4
#         var=sum2/len(a)
#
#         sum3=0
#         sum4=0
#         sum5=0
#         for i in a:
#             sum3=sum3+i**2
#             sum4=sum4+i**3
#             sum5=sum5+i**4
#         u2=sum3/len(a)
#         u3=sum4/len(a)
#         u4=sum5/len(a)
#         u1=mean
#
#         v2=u2-u1**2
#         # v3=u3-3*u2*u1+2*u1**3
#         # v4=u4-4*u3*u1+6*u2*u1**2-3*u1**4
#         #
#         # print(v3)
#         # print(v4)
#
#         v3=sum13/len(a)
#         v4=sum14/len(a)
#         #
#         # print(v3)
#         # print(v4)
#
#         r1=v3/(v2**1.5)
#         r2=v4/(v2**2)
#         #
#         # print(var)
#         # print(v2)
#
#

#         return [mean,var,r1,r2-3]

class Solution():
    def solve(self, a):

        length = len(a)

        temOf2 = 0
        temOf3 = 0
        temOf4 = 0
        sum = 0

        for i in a:
            sum += float(i)
        mean = sum / length

        for i in a:
            temOf2 += (float(i) - mean) ** 2
            temOf3 += (float(i) - mean) ** 3
            temOf4 += (float(i) - mean) ** 4

        if (length != 1):
            f1 = temOf3 / length
            f2 = temOf2 / length
            f2 = f2 ** 1.5
            skew = f1 / f2

            f3 = temOf4 / length
            f4 = temOf2 / length
            f4 = f4 ** 2
            kurt = f3 / f4 - 3
        else:
            skew = 0
            kurt = -3

        if (length == 1):
            var = None
        else:
            var = temOf2 / (length - 1)
            var = round(var, 6)

        mean = round(mean, 6)
        skew = round(skew, 6)
        kurt = round(kurt, 6)
        answer = [mean, var, skew, kurt]
        return answer


solution = Solution()
print(solution.solve([1,2,3]))









