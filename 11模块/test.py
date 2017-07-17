def add(a,b):
	return a + b

# 如果是调用当前.py文件  __name__ == '__main__'
# 如果是ABC调用此模块   __name__ == ABC
# 以下操作为了方便模块开发人员进行内部调试 => 类似于iOS中的单元化测试
if __name__ == '__main__':
	ret = add(3,5)
	print(ret)

'''
至此，可发现test.py中的测试代码，应该是单独执行test.py文件时，才应该执行的，不应该是其他的文件中引用而执行
为了解决这个问题，python在执行一个文件时有个变量__name__
'''