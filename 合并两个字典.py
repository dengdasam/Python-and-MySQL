from collections import Counter
from time import time 


t_1 = time()
aa = {'h':1,'f':2,'t':-1}
bb = {'h':2,'f':4}
for i in range(100000):
	#for k,v in bb.items():
		#if k in aa.keys():
			#aa[k]+=v
		#else:
			#aa[k] = v
			

		
#cc =dict(Counter(aa)+Counter(bb))
	
	cc={}
	for key in aa:
		if bb.get(key):
			cc[key] = aa[key]+bb[key]
		else:
			cc[key] = aa[key]
			
	for key in bb:
		if aa.get(key):
			pass
		else:
			cc[key] = bb[key]	
t_2 = time()
print(cc)
print("耗时{0}".format(t_2-t_1))
	

		


