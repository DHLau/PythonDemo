#coding=utf-8
# 继承
class Cat:
	name = '猫'
	color = 'white'
	def run(self):
		print('%s%s跑起来了'%(self.color,self.name))

class Bosi(Cat):
	def setName(self,newName):
		self.name = newName
	def eat(self):
		print self.name,'在吃饭'

bs = Bosi()
print bs.name
print bs.color
bs.run()
bs.setName('波斯猫')
bs.run()
bs.eat()


