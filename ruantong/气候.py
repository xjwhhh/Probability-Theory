import csv
import numpy as np
from scipy.stats import *
import urllib.request


class Solution():
    def solve(self):
        oldlist = []
        newlist = []
        res = urllib.request.urlopen("http://py.mooctest.net:8081/dataset/temperature/temperature_2010.csv")

        lines = res.readlines()
        for i in range(6, len(lines) - 3):
            ii = lines[i].decode("gbk")
            oldlist.append(float(ii.split(",")[8]))

        res = urllib.request.urlopen("http://py.mooctest.net:8081/dataset/temperature/temperature_2014.csv")

        lines = res.readlines()
        for i in range(5, len(lines) - 3):
            ii = lines[i].decode("gbk")
            newlist.append(float(ii.split(",")[8]))

        oldarray = np.array(oldlist)
        newarray = np.array(newlist)

        list = newarray - oldarray

        d = list.mean()

        n = len(list)

        s = list.var()

        tt = d * np.sqrt(n) / s

        ttt = t.ppf(0.95, n - 1)

        if tt > ttt:
            return 'YES'
        else:
            return 'NO'


solution = Solution()
# solution.solve()
print(solution.solve())
