'''
A large farm wants to try out a new type of fertilizer to evaluate whether it will improve the farm's corn production.
The land is broken into plots that produce an average of 1.215 pounds of corn with a standard deviation of 94 pounds per plot.
The owner is interested in detecting any average difference of at least 40 pounds per plot. How many plots of land would be needed for the experiment if the desired power level is 90%?
Assume each plot of land gets treated with either the current fertilizer or the new fertilizer.
'''

from scipy.stats import norm
import numpy as np

#功效统计
class Solution():
    def solve(self):
        de1 = norm.ppf(0.975)
        de2 = norm.ppf(0.90)
        s = 94
        n = round((s*(2**0.5)*(de1+de2)/40)**2,0)
        # print(n)
        # print(de2)
        # n=((s)*de2/40)**2
        return n

#
# import numpy as np
#
# class Solution():
#     def solve(self):
#         n = 1
#         s = 94
#         while 40 / np.sqrt(2 * (s**2) / n) < (1.28 + 1.96):
#             n += 1
#         return n

solution = Solution()
print(solution.solve())