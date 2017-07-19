#coding=utf-8
class People:
	country = '中国'

	@classmethods
	def setCountry(cls,country):
		print country
		cls.country = country

	@classmethod
	def getCountry(cls):
		return cls.country


p = People()
print p.getCountry() # 可以用过实例对象引用
print People.getCountry() #可以通过类对象引用
p.setCountry('japan')
print p.getCountry()
print People.getCountry()


class People:
    country = 'china'

    @staticmethod
    #静态方法
    def getCountry():
        return People.country

print People.getCountry()



class Cat:
	name = '猫'
	def getName(self):
		print('我是%s'%self.name)
	def setName(self,name):
		self.name = name

cat1 = Cat()
cat1.getName()
cat1.setName('xxx')
cat1.getName()



