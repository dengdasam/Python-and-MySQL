'''
from time import time
def quiksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quiksort(less) + [pivot] + quiksort(greater)
 
a = time()  
ii=[19,10,3,2,55,3,76,4,33,11,322,45,343,23,56,6,5,75,57,5,74,57,54,7,5,87,8,6,1111,12121,323,444]
print(quiksort(ii))
b = time()

print('耗时{0}秒'.format(b-a))
'''
'''
voted = {}
def check_voter(name):
    if voted.get(name):
        print('kick them out')
        
    else:
        voted[name] = True
        print('let them voted')
        
check_voter('hello')
check_voter('nihao')
check_voter('hello')
'''






