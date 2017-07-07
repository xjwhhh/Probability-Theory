'''
A 95% confidence interval for a population mean, u, is given as (18.985, 21.015). This confidence interval is based on a simple random
samples of 36 observations. Calculate the sample mean and standard deviation. Assume that all conditions necessary for inference are
satisfied. Use the t-distribution in any calculations.
'''

from scipy.stats import t
import numpy as np


class Solution():
    def solve(self):
        (lower, higher) = (18.985, 21.015)
        mean = (lower + higher) / 2
        rv = t(35)
        # print(rv.ppf(0.025))
        var = (mean - higher) * (np.sqrt(36) / rv.ppf(0.025))
        mean = round(mean, 2)
        var = round(var, 2)
        return [mean, var]


# class Solution:
#     def solve(self):
#         low = 18.985
#         high = 21.015
#         n = 36
#         alpha = 0.05
#         accuracy = 2
#         aver = (low+high)/2
#         s = (high-aver)*6/t.ppf(1-alpha/2, n-1)
#         return [round(aver,accuracy),round(s,accuracy)]

solution = Solution()
print(solution.solve())
