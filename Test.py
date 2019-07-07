import math


for i in range(1000):
	print(i*math.sqrt(i)**0.5)

print("hello world")

class Dog:
	def __init__(self, age, name):
		
		self.age = age
		self.name =name

	def sayHello(self,n):
		
		print("I am {0},I am {1} years old".format(self.name,self.age))
		
		for i in range(n):
			print(i," hello world")

hh = Dog(16,"hhah")

hh.sayHello(15)