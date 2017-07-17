#coding=utf-8
# 写入数据
f1 = open('test2.txt','w')
f1.write('abcdefghijklmnabcdefghijklmnabcd\nefghijklmnabcdefghijklmnabc\ndefghijklmnabcdefghijklmnabcdefghijklmnabcdefghij\nklmnabcdefghijklmnabcdefghijklmnab\ncdefghijklmnabcdefghijklmnabcdefghijklmn')
f1.close()

# 读取数据 能分段读取
print('\n读取数据 能分段读取read()\n')
f2 = open('test2.txt','r')
content = f2.read(5)
print(content)
print('-'*30)
content = f2.read()
print(content)

# 读数据（readlines）按照行读取
print('\n读数据（readlines）按照行读取\n')
f3 = open('test2.txt','r')
content = f3.readlines()
print(type(content))
i = 0
for temp in content:
	print('%d:%s'%(i,temp))
	i += 1  

# 读数据（readline）
print('\n读数据（readline)\n')
f4 = open('test2.txt','r')
content = f4.readline()
print('1:%s'%content)
content = f4.readline()
print('2:%s'%content)







