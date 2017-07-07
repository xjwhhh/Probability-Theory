'''
Rock-paper-scissors is a hand game played by two or more people where players choose to sign either rock, paper or scissors with their hands.
For your statistics class project, you want to evaluate whether players choose between these three options randomly, or if certain options are favoured above others.
You ask two friends to play rock-paper-scissors and count the time each option is played. The following table summaries the data:

Rock	Paper	Scissors
43	21	35


Use these data to evaluate whether players choose between these three options randomly, or if certain options are favored above others. alpha is 0.05.
'''


#
# import scipy.stats as St
# class Solution():
#     def solve(self):
#         [c,p]=chi2_Fitting([43, 21, 35], [1.0 / 3, 1.0 / 3, 1.0 / 3])
#         return [2,round(c,2),~(p<0.05)]
# #这里四舍五入应该是7.52啊，不知道答案为什么是7.51
#
#
# def chi2_Fitting(array, the_F):
#     c = 0
#     total = sum(array)
#     for i in range(len(array)):
#         c += (array[i] ** 2) / (total * the_F[i])
#     c -= total
#     p = St.chi2.sf(c, len(array) - 1)
#     return [c, p]
#
# so = Solution()
# print (so.solve())

# import numpy
# from scipy.stats import chi2
#
# class Solution():
#     def solve(self):
#         k = 3
#         alpha = 0.05
#         chi = self.tool(43, 33) + self.tool(21, 33) + self.tool(35, 33)
#         return [k-1, round(chi,2), chi<chi2.ppf(1-alpha,k-1)]
#
#     def tool(self, e, t):
#         return numpy.square(e - t) / t
#
#
# solution = Solution()
# print(solution.solve())

import scipy.stats as stats


class Solution():
    def solve(self):
        a = [43, 21, 35]
        alpha = 0.05
        kafang = stats.chisquare(a)
        df = len(a) - 1

        print(kafang)

        if kafang[1] < alpha:
            result = False
        else:
            result = True
        # print kafang
        # print [df, round(kafang[0], 2), result]
        return [df, round(kafang[0], 2), result]

solu = Solution()
print(solu.solve())


