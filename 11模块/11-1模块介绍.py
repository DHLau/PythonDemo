import math
# Python的from语句让你从模块中导入一个指定的部分到当前命名空间中。
from fib import fibonacci

# 把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
# 这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。
from modname import *

'''
	当你导入一个模块，Python解析器对模块位置的搜索顺序是：
		当前目录
		如果不在当前目录，Python则搜索在shell变量PYTHONPATH下的每个目录。
		如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/
		模块搜索路径存储在system模块的sys.path变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。
'''