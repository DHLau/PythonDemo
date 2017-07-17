#coding=utf-8
oldFileName = raw_input('请输入您要拷贝的文件名称')
oldFile = open(oldFileName,'rb') # 以二进制的形式进行读取
if oldFile:
	# 提取文件的后缀
	# 方法1
	#fileSuffix = oldFileName.rfind('.')
	#print(oldFileName[fileSuffix:])
	# 方法2
	fileNameList = oldFileName.split('.')
	fileSuffix = '.' + fileNameList[len(fileNameList) - 1]


	# 组织新的文件名
	newFileName = fileNameList[0] + '副本' + fileSuffix
	print(newFileName)


	# 创建新文件
	newFile = open(newFileName,'wb')

	# 把旧文件中的数据写入到新文件中
	for lineContent in oldFile.readlines():
		newFile.write(lineContent)

	# 关闭文件
	oldFile.close()
	newFile.close()







