# -*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''

class Solution():
	def solve(self, A):
		#use isPalindrom function to check if the string is palindrome or not
		list = []
		for i in A:
			if self.isPalindrome(i) == True:
				list.append(i)
        	return list


	def isPalindrome(self,x):
		if (str(x) == str(x)[::-1]):
			return True
		else:
			return False

A=['123', '232', '4556554', '12123', '3443','1314131']
object = Solution()
print(object.isPalindrome(232))
print(object.solve(A))