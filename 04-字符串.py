#coding=utf-8

# 输出字符串
name = 'liudh'
job = '程序猿'
print('姓名%s'%name)

# 输入字符串
'''
username = raw_input('请输入用户名')
password = raw_input('请输入密码')
print('用户名%s'%username)
print('密码%i'%int(password))

'''

#字符串索引
aLongStr = 'abcdefghijklmnopqrstuvwxyz'
print(aLongStr[0])
print(aLongStr[0:3]) #取下标0-2的字符 abc
print(aLongStr[2:4]) #取下标2-3的字符 cd
print(aLongStr[2:])  #从下标2 开始取  一直到 最后  cdefghijklmnopqrstuvwxyz 
print('\n')
#格式化字符串
'''
	格式符号	转换
	%c	字符
	%s	通过str() 字符串转换来格式化
	%i	有符号十进制整数
	%d	有符号十进制整数
	%u	无符号十进制整数
	%o	八进制整数
	%x	十六进制整数（小写字母）
	%X	十六进制整数（大写字母）
	%e	索引符号（小写'e'）
	%E	索引符号（大写“E”）
	%f	浮点实数
	%g	％f和％e 的简写
	%G	％f和％E的简写
'''

#字符串常见操作

# 1.find
# 检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1
print('find')
print(aLongStr.find("wwe",0,len(aLongStr)))
print(aLongStr.find("yz",0,len(aLongStr)))

# 2.index 
# 跟find()方法一样，只不过如果str不在 mystr中会报一个异常.
print('\nindex')
print(aLongStr.index("ijk",0,len(aLongStr)))

# 3.count 
# 返回 str在start和end之间 在 mystr里面出现的次数
print('\ncount')
print(aLongStr.count('a'))

# 4.replace
# 把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.
print('\nreplace')
testStr = aLongStr + 'abc'
print(testStr.replace('abc','ABC',2))

# 5.split
# 以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
print('\nsplit')
testSplitStr = 'hello world ha ha'
print(testSplitStr.split(' ',2))

# 6.capitalize
# 把字符串的第一个字符大写
print('\ncapitalize')
testCapitalizeStr = aLongStr
print(testCapitalizeStr.capitalize())

# 7.startswith
# 检查字符串是否是以 obj 开头, 是则返回 True，否则返回 False
print('\nstartswith')
print(aLongStr.startswith('abc'))

# 8.endswith
# 检查字符串是否以obj结束，如果是返回True,否则返回 False.
print('\nendswith')
print(aLongStr.endswith('xyz'))

# 9.lower
# 转换 mystr 中所有大写字符为小写
testLowerStr = 'ABCDeFGHI'
print('\nlower')
print(testLowerStr.lower())

# 10.upper
# 转换 mystr 中的小写字母为大写
testUpperStr = 'abcdefgHIJKLMN'
print('\nupper')
print(testUpperStr.upper())

# 11.ljust
# 返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
print('\nljust')
testLjustStr = 'ldh'
print(testLjustStr.ljust(10))


# 12.rjust
# 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
print('\nrjust')
testRjustStr = 'ldh'
print(testRjustStr.rjust(10))


# 13.center
# 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
print('\ncenter')
testCenterStr = 'ldh'
print(testCenterStr.center(10))


# 14.lstrip
# 删除 mystr 左边的空格
print('\nlstrip')
testLstrip = '    ldh'
print(testLstrip.lstrip())


# 15.rstrip
# 删除 mystr 字符串末尾的空格
print('\nrstrip')
testRstripStr = '    ldh    '
print(testRstripStr.rstrip())


# 16.rfind
# 从右边开始查找 类似于 find()函数，不过是从右边开始查找.
print('\nrfind')
print(aLongStr.rfind('z')) #25


# 17.rindex
# 从右边 类似于 index()，不过是从右边开始.
print('\nrindex')
print(aLongStr.rindex('z'))


# 18.partition
# 把mystr以str分割成三部分,str前，str和str后
print('\npartition')
testPartitionStr = 'first second third fourth'
print(testPartitionStr.partition('second'))


# 19.rpartition
# 类似于 partition()函数,不过是从右边开始.
print('\nrpartition')
testRpartitionStr = 'first second third fourth'
print(testRpartitionStr.rpartition('second'))


# 20.splitlines
# 按照行分隔，返回一个包含各行作为元素的列表
print('\nsplitlines')
testSplitlines = 'first\nsecond\nthird\nfourth\n'
print(testSplitlines.splitlines())


# 21.isalnum
# 如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False
print('\n isalnum')
testIsalnum = 'abc'
testIsalnum2 = '123'
testIsalnum3 = 'abc123'
print(testIsalnum.isalnum())
print(testIsalnum2.isalnum())
print(testIsalnum3.isalnum())


# 22.isalpha()
# 如果 mystr 所有字符都是字母 则返回 True,否则返回 False
print('\n isalpha()')
testIsalphaStr1 = 'abc'
testIsalphaStr2 = 'abc123'
print(testIsalphaStr1.isalpha())
print(testIsalphaStr2.isalpha())


# 23.isdigit
# 如果 mystr 只包含数字则返回 True 否则返回 False
print('\n isdigit()')
testIsdigitStr1 = 'abc'
testIsdigitStr2 = 'abc123'
print(testIsdigitStr1.isdigit())
print(testIsdigitStr2.isdigit())


# 24.isspace
# 如果 mystr 中只包含空格，则返回 True，否则返回 False.
print('\n isspace')
testIsspaceStr1 = '   '
testIsspaceStr2 = '   asd'
print(testIsspaceStr1.isspace())
print(testIsspaceStr2.isspace())



# 25.isupper
# 如果 mystr 所有字符都是大写，则返回 True，否则返回 False
print('\n isupper')
testIsupperStr1 = 'ABC'
testIsupperStr2 = 'aAsd'
print(testIsupperStr1.isupper())
print(testIsupperStr2.isupper())




