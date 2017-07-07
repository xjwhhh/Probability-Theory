import csv
import numpy as np
from scipy.stats import *
import urllib.request


# class Solution():
#     def solve(self):
#         oldlist = []
#         newlist = []
#         res = urllib.request.urlopen("http://py.mooctest.net:8081/dataset/air/air_quality_2010.csv")
#
#         lines = res.readlines()
#         for i in range(8, len(lines)):
#             ii = lines[i].decode("gbk")
#             # print(ii)
#             if len(ii) > 10:
#                 oldlist.append(int(ii.split(",")[4]))
#
#         res = urllib.request.urlopen("http://py.mooctest.net:8081/dataset/air/air_quality_2014.csv")
#
#         lines = res.readlines()
#         for i in range(7, len(lines) - 3):
#             ii = lines[i].decode("gbk")
#             if len(ii) > 10:
#                 newlist.append(int(ii.split(",")[7]))
#
#         oldarray = np.array(oldlist)
#         newarray = np.array(newlist)
#
#         # print(oldarray)
#         # print(newarray)
#
#         list = newarray - oldarray
#         d = list.mean()
#         # print(d)
#         n = len(list)
#         s = list.var()
#         s=s*n/(n-1)
#         tt = d * np.sqrt(n) / (s ** 0.5)
#         print(tt)
#         ttt = t.ppf(0.05, n - 1)
#         if tt > ttt:
#             return [tt, 'NO']
#         else:
#             return [tt, 'YES']



import numpy as np
import scipy.stats as stats

class Solution():
    def solve(self):
        l2010 = [285,307,318,296,346,328,340,311,334,315,327,321,353,347,295,322,301,333,347,362,365,303,315,347,365,361,304,236,280,328,262]
        l2014 = [167,145,49,162,213,215,230,239,246,198,212,180,343,230,79,134,161,196,259,275,342,207,139,278,329,341,157,193,216,249,184]
        n = len(l2010)
        l2010NP = np.array(l2010)
        l2014NP = np.array(l2014)
        d = l2014NP - l2010NP
        mean = d.mean()
        sdev = (d.var() * n / (n - 1)) ** 0.5

        alpha = 0.05  # use t-distribution

        t = mean / (sdev / (n ** 0.5))
        tp = stats.t.ppf(1 - alpha, n - 1)

        print(t)

        if t >= tp:
            return [t, 'NO']
        else:
            return [t, 'YES']

solution = Solution()
print(solution.solve())
