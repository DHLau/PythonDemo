#coding=utf-8
'''
多态的概念是应用于Java和C#这一类强类型语言中，而Python崇尚“鸭子类型”。

所谓多态：定义时的类型和运行时的类型不一样，此时就成为多态

'''
class F1:
  pass
  
class S1(F1):

  def show(self):
      print 'S1.show'

class S2(F1):

  def show(self):
      print 'S2.show'

def Func(obj):
  print obj.show()

s1_obj = S1()
Func(s1_obj) 

s2_obj = S2()
Func(s2_obj)