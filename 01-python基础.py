#coding=utf-8
# 我是一行注释
'''
	我是多行注释
	我是多行注释
	我是多行注释
'''
print('--------分割线-------')


num1 = 100
num2 = 87
result = num1 + num2
print(result)
print(type(result))
# 在python中，只要定义了一个变量，而且它有数据，那么它的类型就已经确定了，不需要咱们开发者主动的去说明它的类型，系统会自动辨别
#使用 type 查看数据类型 

password = raw_input("请输入密码")
print "您刚刚输入的密码是:",password

num3 = 99 
num4 = 44
print(num3 // num4) #num3 对 num4 求余数后 整数部分
print(num3 % num4)  #num3 对 num4 求余数后 余数部分

'''
+=	加法赋值运算符	c += a 等效于 c = c + a
-=	减法赋值运算符	c -= a 等效于 c = c - a
*=	乘法赋值运算符	c = a 等效于 c = c a
/=	除法赋值运算符	c /= a 等效于 c = c / a
%=	取模赋值运算符	c %= a 等效于 c = c % a
**=	幂赋值运算符	c **= a 等效于 c = c ** a
//=	取整除赋值运算符	c //= a 等效于 c = c // a
'''
