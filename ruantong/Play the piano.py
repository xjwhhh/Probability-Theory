'''
 Georgianna claims that in a small city renowned for its music school, the average child takes at least 5 years of piano lessons.
 We have a random sample of 20 children from the city with a mean of 4.6 years of piano lessons and a standard deviation of 2.2 years.
 Evaluate Georgianna's claims using a hypothesis test. alpha is 0.05.

Extra:

(1) Construct a 95% confidence interval for the number of years students in this city takes piano lessons and interpret it in context of the data.

(2) Do your results from the hypothesis test and the confidence interval agree? Explain your reasoning.
'''


from scipy.stats import t as T
import numpy as np
class Solution():
    def solve(self):
        mean = 4.6
        u = 5
        var = 2.2
        n = 20
        rv = T(n - 1)
        t = (mean - u) / (var / np.sqrt(n))
        test = rv.ppf(0.95)
        return [n - 1, round(t, 2), (t < test)]

solution = Solution()
print(solution.solve())