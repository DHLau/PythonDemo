#coding=utf-8
class A:
	name = '小李'
	def run(self):
		print('------A-----%s'%self.name)

class B:
	name = '小明'
	def eat(self):
		print('------eat----%s'%self.name)


class C(A,B):
	def drink(self):
		print('------drink-------')

obj_c = C()
obj_c.drink()
obj_c.run()
obj_c.eat()








