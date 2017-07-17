#coding=utf-8

# 获取当前读写的位置
'''
	在读写文件的过程中，如果想知道当前的位置，可以使用tell()来获取
'''
f = open('test.txt','r')
str = f.read(3)
print str

position = f.tell()
print "文件当前位置为:",position

str = f.read(3)
print str

position = f.tell()
print "文件当前位置为",position

f.close()



# 定位到某个位置
'''
	如果在读写文件的过程中，需要从另外一个位置进行操作的话，可以使用seek()
	seek(offset, from)有2个参数
	offset:偏移量
	from:方向
	0:表示文件开头
	1:表示当前位置
	2:表示文件末尾
'''
f1 = open('test.txt','w')
f1.write('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
f1 = open('test.txt','r')
str = f1.read(30)
print('读取的数据为%s'%str)
f1.seek(0,0)
str = f1.read(30)
print('读取的数据为%s'%str)

# 重新设置位置
f1.seek(-3,2)

# 读取到的数据为：文件最后3个字节数据
str = f1.read()
print "读取的数据是 : ", str
f1.close()








