'''
The table below summaries a data set that examines the response of a random sample of college graduates and non-graduate on the topic of oil drilling.
Complete a chi-square test for test data to check whether there is a statistically significant difference in responses from college graduates and non-graduates.

College Grad?	Yes	No	Total
Support	154	132	286
Oppose	180	126	306
Do not know	104	131	235
Total	438	389	827

'''

import numpy as np
import scipy.stats as St


class Solution():
    def solve(self):
        [chi, p] = chi2_Independance([154, 180, 104], [132, 126, 131])
        chi=round(chi,2)
        # print(chi)
        # print(p)
        return [2, chi, p > 0.01]


def chi2_Independance(*arg):
    c = len(arg)
    r = len(arg[0])
    arg = np.array(arg)
    # print(arg)
    row = list(sum(arg))
    # print(row)
    col = [sum(arg[i]) for i in range(c)]
    # print(col)
    total = float(sum(row))
    # print(total)
    chi_sta = 0
    for i in range(c):
        for j in range(r):
            chi_sta += (arg[i][j] - col[i] * row[j] / total) ** 2 / (col[i] * row[j] / total)
    p = St.chi2.sf(chi_sta, (r - 1) * (c - 1))
    # print(St.chi2.sf(20.09,8))
    # print(p)
    return [chi_sta, p]


# import numpy as np
# import scipy.stats as stats
#
#
# class Solution():
#     def solve(self):
#         alpha = 0.05
#         row1 = [154, 132]
#         row2 = [180, 126]
#         row3 = [104, 131]
#         data = [row1, row2, row3]
#         kafang = stats.chi2_contingency(data)
#         print(kafang)
#         # print kafang
#         df = kafang[2]
#         high = stats.chi.ppf(1 - alpha, df)
#         print (df)
#         print (kafang[0])
#         print (high)
#         if kafang[0] >= high:
#             result = False
#         else:
#             result = True
#         return [df, round(kafang[0], 2), result]


so = Solution()
print (so.solve())
