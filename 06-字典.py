#coding=utf-8
info={'name':'班长','id':100,'sex':'fff','address':'地球'}
print(info['name'])

# 相关操作(增删改查)
#       修改
info['name'] = 'ldh'
print(info)

#       添加
# 如果在使用 变量名['键'] = 数据 时，这个“键”在字典中，不存在，那么就会新增这个元素
info['age'] = 18
print(info)

# 对字典进行删除操作，有一下几种：del clear()
# demo:del删除指定的元素
print 'del删除前',info
del info['name']
print 'del删除后',info

# clear
info2 = info
print 'clear删除前',info2
info2.clear()
print 'clear删除后',info2


# 相关操作2
# len 
dict1 = {'name':'班长','id':100,'sex':'fff','address':'地球'}
print(len(dict1))
# keys
print(dict1.keys()) 
# values
print(dict1.values())
# items 返回一个元组
print(dict1.items())
# has_key(key)
print(dict1.has_key('name'))


# 遍历
for key in dict1.keys():
	print(key)
for value in dict1.values():
	print(value)
for item in dict1.items():
	print(item)
for key,value in dict1.items():
	print('key=%s,value=%s'%(key,value))









