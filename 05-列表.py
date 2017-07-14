#coding=utf-8
arr1 = ['xiaoming','xiaohong','xiaozhang']
print(arr1[0])
print(arr1[1])
print(arr1[2])
for item in arr1:
	print(item)

# 列表相关操作
# 增 append
arr1.append('ldh')
print(arr1)

# 改 
arr1[3] = 'wtt'
print(arr1)

# 查
if 'wtt' in arr1:
	print('找到了')
else:
	print('没找到')

# 删
arr2 = arr1
print(arr2)

#    del 删除指定索引
del arr2[0]
print(arr2)

#    pop 删除最后一个
arr2.pop()
print(arr2)

#    remove 删除指定元素
arr2.remove('xiaohong')
print(arr2)






