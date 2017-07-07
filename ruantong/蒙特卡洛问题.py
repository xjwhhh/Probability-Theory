#-*- coding:utf-8 -*-
'''
log api example: log('output is: ' + str(output))
'''
import random
'''
You can delete the MontyCarlo and write your Monty Carlo
下面为利用蒙特卡罗方法计算π的python实现代码，请仔细阅读，理解代码含义，并试着写出你自己版本的计算π的蒙特卡罗方法
用计算机随机模拟求得某种概率
'''

#this function may spend a little time to execute
def MontyCarlo():
    n = 1000000
    k = 0
    for i in range(n):
        x = random.uniform(-1, 1)#用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。如果a > b，则生成的随机数n: a <= n <= b。如果 a <b， 则 b <= n <= a。
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            k = k + 1#落入园内
    return 4 * float(k) / float(n)#pi=4*p,面积为4的正方形内园

if __name__ == '__main__':
    pi = MontyCarlo()
    #print out the result
    print(pi)