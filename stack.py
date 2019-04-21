#coding:utf-8

class Stack(object):
	'''栈'''
	def __init__(self):
		'''初始化一个栈'''
		self.__list = []

	def push(self,item):
		'''入栈'''
		self.__list.append(item)

	def pop(self):
		'''弹出'''
		return self.__list.pop()

	def peek(self):
		'''返回栈顶元素'''
		if self.__list:
			return self.__list[-1]
		else:
			return None

	def is_emperty(self):
		'''判断是否为空'''
		return self.__list == []

	def size(self):
		'''栈的大小'''
		return len(self.__list)

if __name__ == '__main__':
	stack1 = Stack()
	stack1.push(1)
	stack1.push(2)
	print 'size : ',stack1.size()
	stack1.push(3)
	stack1.push(4)
	stack1.push(5)
	print stack1.peek()
	print stack1.pop()
	print stack1.pop()
	print stack1.pop()
	print stack1.pop()
	print stack1.pop()
	print 'size ',stack1.size()
	print stack1.peek()




