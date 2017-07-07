import numpy as np

class Solution():
    def solve(self, A):
        f = np.array([2.0, 0.0, -1.0, 1.0])
        g = np.poly1d(f) * np.poly1d(A)
        t=np.poly1d([2.0,4.0,1.0,-1.0,1.0,1.0])
        print(t)
        return np.poly1d(g)


object = Solution()
# A = np.poly1d([2.0, 4.0, 1.0, -1.0, 1.0, 1.0])
A=np.array([1.0, 2.0, 1.0])
print(object.solve(A))
