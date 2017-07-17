#coding=utf-8

# 缺省参数(默认参数)
def printinfo(name, age = 35):
    # 打印任何传入的字符串
	print "Name: ", name
	print "Age ", age
# 调用printinfo函数
printinfo(name="miki")
printinfo(age=9,name="miki")

# 不定长参数
def printinfo2(arg1,*vartuple):
	print "输出"
	print(arg1)
	for arg in vartuple:
		print(arg)
printinfo2(1,2,3,4)


# 函数的嵌套使用
def testB():
	print '---- testB start----'
	print '这里是testB函数执行的代码...(省略)...'
	print '---- testB end----'
def testA():
	print '---- testA start----'
	testB()
	print '---- testA end----'
testA()


# 局部变量和全局变量
# 如果一个变量，既能在一个函数中使用，也能在其他的函数中使用，这样的变量就是全局变量
# 在函数外边定义的变量叫做全局变量
# 全局变量能够在所以的函数中进行访问
# 如果在函数中修改全局变量，那么就需要使用global进行声明，否则出错
# 如果全局变量的名字和局部变量的名字相同，那么使用的是局部变量的，小技巧强龙不压地头蛇
a = 20
def test1():
	global a
	print('修改后%i'%a)
	a = 30
	print('修改后%i'%a)
test1()


# 递归函数
def sum(num):
	if num == 1:
		return 1
	else:
		return num * sum(num-1);
print(sum(5))



