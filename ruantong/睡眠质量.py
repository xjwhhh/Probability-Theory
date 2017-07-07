import numpy as np
from scipy.stats import norm


class Solution():
    def solve(self):
        aver=8.5
        n=3600
        var=25
        z = norm.ppf(0.975)
        low=aver-np.sqrt(var)*z/np.sqrt(n)
        high=aver+np.sqrt(var)*z/np.sqrt(n)
        return [low,high]
solution = Solution()
print(solution.solve())