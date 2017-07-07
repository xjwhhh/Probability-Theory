'''
New York is known as "the city that never sleeps". A random sample of 25 New Yorkers were asked how much sleep they get per night.
Statistical summaries of these data are shown below.
Do these data provide strong evidence that New Yorkers sleep less than 8 hours per night on average?

Null-hypothesis is H0: u=8, and alpha is 0.05

n	mean	stand-variance	min	max
25	7.73	0.77	6.17	9.78


Extra:

(1) If you were to construct a 90% confidence interval that corresponded to this hypothesis test, would you expect 8 hours to be in the interval? Explain your reasoning.
'''

from scipy.stats import t as T
import numpy as np
class Solution():
    def solve(self):
        u = 8
        (n, mean, stand_variance, min, max) = (25, 7.73, 0.77, 6.17, 9.78)
        t = (mean - u) / (stand_variance / np.sqrt(n))
        rv = T(n - 1)
        test = rv.ppf(0.05)
        # print(test)
        return [n - 1, round(t, 2), (t > test)]


solution = Solution()
print(solution.solve())
