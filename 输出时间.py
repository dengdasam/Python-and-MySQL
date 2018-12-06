import time
coun = 0
while True:
    a = time.strftime("%H:%M:%S",time.localtime())
    coun += 1
    time.sleep(5)
    print("现在是第{0}次报时".format(coun))
    print(a)