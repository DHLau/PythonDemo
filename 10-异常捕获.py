#coding=utf-8
import time

try: 
	print('---------test-------1')
	open('123.txt','r')
	print('---------test-------2')
except IOError:
	pass

try:
	print num
except NameError, errorMsg:
	print '产生错误了;', errorMsg


try:
    print '-----test--1---'
    # 如果123.txt文件不存在，那么会产生 IOError 异常
    open('123.txt','r')
    print '-----test--2---'
    # 如果num变量没有定义，那么会产生 NameError 异常
    print num
except (IOError,NameError), errorMsg: 
    #如果想通过一次except捕获到多个异常可以用一个元组的方式

    # errorMsg里会保存捕获到的错误信息
    print errorMsg


# try...finally...

try:
    f = file('poem.txt')
    while True: # our usual file-reading idiom
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print line,


finally:
    f.close()
    print 'Cleaning up...closed the file'


# else
 try:
        num = 100
        print num
    except NameError, errorMsg:
        print('产生错误了:%s'%errorMsg)
    else:
        print('没有捕获到异常，真高兴')
    finally:
        print('我一定会执行的哦')




