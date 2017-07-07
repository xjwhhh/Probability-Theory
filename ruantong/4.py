class Solution():
    # def solve(self,A):
    #     # list={'pear':0, 'banana':0, 'cherry':0, 'peach':0, 'pineapple':0, 'apple':0}
    #     list={}
    #     for i in A:
    #         if i in list:
    #             list[i]=list[i]+1
    #         else:
    #             list[i]=1
    #     return list
    def solve(self, A):
        if len(A) == 0:
            return {}
        B = [A[0]]
        for i in A:
            for j in B:
                if i != j:
                    B.append(i)
        m = 0
        for i in B:
            m = m + 1
        dict = {}
        for i in range(0, m):
            dict[B[i]] = A.count(B[i])
        return dict

object = Solution()
A = ['apple', 'banana', 'cherry', 'pineapple', 'banana', 'peach', 'pear','peach', 'cherry' ]
print(object.solve(A))
