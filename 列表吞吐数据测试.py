import time

t0 = time.clock()            
#li = []
#for i in range(1,1000000):
    #if i % 2 == 0:
        #li.append(i)
        
li = [i for i in range(1,1000000) if i%2 == 0]




t1 = time.clock()
print("运行时间%s s"%(t1-t0))