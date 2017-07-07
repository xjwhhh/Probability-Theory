import csv

import numpy as np

from scipy.stats import *

import urllib.request


class Solution():
    def solve(self):
        manlist = []
        womanlist= []
        genderbi=[]
        genderbi1=[]
        genderbi2=[]
        genderbi3=[]

        res = urllib.request.urlopen("http://py.mooctest.net:8081/dataset/population/population_gender.csv")
        lines = res.readlines()
        for i in range(4, len(lines)):
            ii = lines[i].decode("gbk")
            manlist.append(int(ii.split(",")[2]))
            womanlist.append(int(ii.split(",")[3]))
            genderbi.append(float(ii.split(",")[4]))
            genderbi1.append(float(ii.split(",")[8]))

        gender=np.array(genderbi)
        mean1=gender.mean()
        var=gender.var()
        alpha=0.1
        n=len(gender)
        lower=mean1-var**0.5*norm.ppf(1-alpha/2)/np.sqrt(n)
        higher=mean1+var**0.5*norm.ppf(1-alpha/2)/np.sqrt(n)

        print(genderbi1)

        tt=t.ppf(0.95,len(genderbi1)*2-2)
        print(tt)






        return [[lower,higher],[]]



solution = Solution()
print(solution.solve())