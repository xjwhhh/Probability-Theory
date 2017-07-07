# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''



class Solution():

    # def solve(self, A):
    #     list=[0,0,0,0,0,0,0,0,0,0]
    #     for numberstr in A:
    #         number = int(numberstr)
    #         while (number > 0):
    #             a = int(number % 10)
    #             list[a] = list[a] + 1
    #             number = int(number / 10)
    #         se={}
    #         for i in range(0,len(list)):
    #             se[i]=list[i]
    #     print(str(se))

    def solve(self, A):
        s = ""
        for i in A:
            s += i
        list = {0: s.count('0'), 1: s.count('1'), 2: s.count('2'), 3: s.count('3'), 4: s.count('4'), 5: s.count('5'),
                6: s.count('6'), 7: s.count('7'), 8: s.count('8'), 9: s.count('9')}
        return list



so=Solution()
t=['12','34','567', '36','809','120']
so.solve(t)