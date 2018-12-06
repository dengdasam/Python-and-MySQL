import time
target=int(input("请输入数列值个数："))
start_1 = time.time()
ii = []
res=0
a,b=1,1
for i in range(target-1):
    a,b=b,a+b
    ii.append(a)
end_1 = time.time()
print(ii)
print("耗时：{0} s".format(end_1-start_1))

