def jiami():
	fileName = input('请输入要加密的文件名')
	while True:
		try:
			password = int(input('请输入一个数字作为密码'))
			break
		except:
			print('please input a number')
	# 打开文件
	fileWord = open(fileName,'r+')
	# 查找文件的后缀位置
	num = fileName.rfind('.')
	# 进行名字修改
	newFileName = fileName[0:num] + '[加密]' + fileName[num:]
	# 防止文件独处内容过大,一部分的读
	content = fileWord.read(1)
	newFile = open(newFileName,'a+')
	i=0
	while len(content)>0:
		# 将变量转换成整形
		contentInt = ord(content)
		# 进行加密
		newContentInt = contentInt + password # 密码

		# 转换成字符
		c = chr(newContentInt)
		# 写入
		newFile.write(c)
		content = fileWord.read(1)
		i+=1
	# 关闭文件
	newFile.close()
	fileWord.close()

def jieMi():
	# 获取文件和密码
	fileName = raw_input('请输入要解密的文件名')
	# 密码输入
	while True:
		try:
			password = int(raw_input('请输入一个数字作为密码'))
		except :
			print('please input a number')
	# 打开文件
	fileWord = open(fileName,'r+')
	# 查找文件的后缀位置
	num = fileName.rfind('.')
	# 查找[加密]字样
	num1 = fileName.rfind('[')
	# 进行名字修改
	newFileName = fileName[0:num1] + '[解密]' + fileName[num:]
	# 打开一个新的文件
	newFile = open(newFile,'a+')
	# 防止独处内容过大,一部分一部分的读
	content = fileWord.read(1)
	i = 0
	while len(content)>0:
		# 将变量转成整形
		contentInt = ord(content)
		# 进行加密
		newContentInt = contentInt - password # 密码
		# 转换成字符
		c = chr(newContentInt)
		# 写入
		newFile.write(c)
		content = fileWord.read(1)
		i+=1
	newFile.close()
	fileWord.close()

while  True:
	try:
		work = int(raw_input('please choose your work is (1-加密, 2-解密,3-退出 : )'))
	except :
		print('please try again')
		continue

	if work == 1:
		jiami()
		print('加密成功')
	elif work == 2:
		jieMi()
		print('解密成功')
	elif work = 3:
		break
	else :
		pass























