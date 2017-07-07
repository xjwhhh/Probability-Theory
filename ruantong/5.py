class Solution():
    def solve(self, A):
        # call function prime
        list = []
        for i in A:
            if self.prime(i)==True:
                list.append(i)
        return list

    def prime(self, x):
        if x <= 1:
            return False
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

A = [2,3,4,5,6,7,8,9]
object = Solution()
print(object.solve(A))
