#coding=utf-8
class Car:
	# 公有属性
	wheelNum = 4
	color = 'red'

	# 私有属性
	__owner = '张学友'

	#方法
	def getCarInfo(self):
		print('车轮子个数%d,车的颜色%s'%(self.wheelNum,self.color))
	def run(self):
		print('车在跑')

# 创建对象
BWM = Car()
# 访问属性
print(BWM.wheelNum)
# print(BWM.__owner)
# 调用方法
BWM.getCarInfo()



'''
提示找不到该属性，因为私有属性是不能够在类外通过对象名来进行访问的。在Python中没有像C++中public和private这些关键字来区别公有属性和私有属性，它是以属性命名方式来区分，如果在属性名前面加了2个下划线'__'，则表明该属性是私有属性，否则为公有属性（方法也是一样，方法名前面加了2个下划线的话表示该方法是私有的，否则为公有的）。
'''

class Child:
	__name = '小明'
	__age = 3

	def getAge(self):
		return self.__age
	def getName(self):
		return self.__name

xiaoming = Child()
print xiaoming.getAge(), xiaoming.getName()



class Animal:
	def setAnimalName(self,name):
		self.name = name
	def getAnimalName(self):
		print('我的名字是%s'%self.name)

dog = Animal()
dog.setAnimalName('旺财')
dog.getAnimalName()


cat = Animal()
cat.setAnimalName('喵喵')
cat.getAnimalName()


# 构造函数
class NewCar:
	def __init__(self,wheelNum,color):
		self.wheelNum = wheelNum
		self.color = color
	def run(self):
		print('我是%d驱,我的颜色是%s'%(self.wheelNum,self.color))

tesla = NewCar(4,'yellow')
tesla.run()


# 析构方法
class Animal2:
	def __init__(self):
		print('构造方法被调用')
	def __del__(self):
		print('析构方法被调用')
dog2 = Animal2()
del dog2




