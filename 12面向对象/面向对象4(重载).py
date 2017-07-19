#coding=utf-8
#所谓重载，就是子类中，有一个和父类相同名字的方法，在子类中的方法会覆盖掉父类中同名的方法
class Cat:
	def eat(self):
		print('我是一只普通的小猫,喜欢吃🐟')

class Bosi(Cat):
	def eat(self):
		print('我是一个波斯猫,喜欢吃猫粮')

bosi1 = Bosi()
bosi1.eat()


