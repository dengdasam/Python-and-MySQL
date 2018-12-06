import time

t0 = time.clock()

number = 10
number += 10

b = 10**number

x1 = b*4//5
x2 = b//-239

sum_1 = x1 + x2

number *= 2

for i in range(3,number,2):
    x1 //= -25
    x2 //= -57121
    x = (x1 + x2) // i
    sum_1 += x
    
pai = sum_1*4

pai //= 10**10

result = str(pai)[0] + "."+ str(pai)[1:len(str(pai))]

print(result)
t1 = time.clock()

print(" 运行耗时： %s s"%(t1-t0))