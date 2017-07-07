import csv

import numpy as np

from scipy.stats import *

import urllib.request


class Solution():
    def solve(self):
        oldlist2 = []
        totallist2 = []
        res = urllib.request.urlopen("http://py.mooctest.net:8081/dataset/population/population_old.csv")
        lines = res.readlines()
        for i in range(3, len(lines)):
            ii = lines[i].decode("gbk")
            oldlist2.append(int(ii.split(",")[1]))
        res = urllib.request.urlopen("http://py.mooctest.net:8081/dataset/population/population_total.csv")
        lines = res.readlines()
        for i in range(5, len(lines)):
            ii = lines[i].decode("gbk")
            totallist2.append(int(ii.split(",")[4]))

        oldold = []
        for i in range(len(oldlist2)):
            oldold.append(oldlist2[i] * 100 / totallist2[i])
        array = np.array(oldold)
        n = len(oldold)
        aver = array.mean()
        s = array.var()
        lower = aver - s ** 0.5 * t.ppf(0.95, 30) / np.sqrt(n)
        higher = aver + s ** 0.5 * t.ppf(0.95, 30) / np.sqrt(n)
        lower2 = (n - 1) * (s) / (chi.ppf(0.95, n - 1) ** 2)
        higher2 = (n - 1) * (s) / (chi.ppf(0.05, n - 1) ** 2)
        return [[lower, higher], [lower2, higher2]]
