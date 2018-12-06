#算法改进-1

import math
import time
def primesqrt(n):

    result = []



    result.append(2)

    result.append(3)


    for i in range(5,n+1,2):

        for j in range(2,int(math.sqrt(i))+2):

            #for j in range(2,(i>>4)+1):

            if i%j == 0:

                break

            else:

                result.append(i)

    return result

def primeSolver(min,max):
    li_prime = primesqrt(max)

    li_prime = [i for i in li_prime if i > min]




    with open("num_1.txt","w+") as num:
        for index,value in enumerate(li_prime):
            num.write(str(index+1) + "->" + str(value)+"\n")

t0 = time.clock()            
primeSolver(0,1000000)
t1 = time.clock()
print("运行时间%s s"%(t1-t0))