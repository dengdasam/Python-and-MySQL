# 算法改进—2
import time

class Solution:
    def countPrimes(self, n):
        if n < 2:
            return 0     # 注意 数组越界的情况

        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5)+1):    # 在选择除数时候的一个小技巧.大于一半的数是不可能做除数的. 事实证明, 能够节省400ms的时间
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])  # 非常简洁的语句, 从小到大用埃氏筛法, 将每一个不是宿舍的数筛选掉.大大减少出发的数量.
        return primes


def primeNum(min,max):

    aa = Solution()

    li_2 = aa.countPrimes(max)
    li = [i for i in range(len(li_2)) if li_2[i] == True]
    li = [i for i in li if i > min]

    with open("num_2.txt","w+") as num:
        for index,value in enumerate(li):
            num.write(str(index+1) + "->" + str(value) + "\n")
            
t0 = time.clock()                       
primeNum(0,1000000)
t1 = time.clock()
print("运行时间%s s"%(t1-t0))