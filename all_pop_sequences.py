#coding=utf8


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

	def is_empty(self):
		'''判断是否为空'''
		return self.__list == []

	def size(self):
		'''栈的大小'''
		return len(self.__list)


class Queue(object):
	"""队列"""
	def __init__(self):
		"""初始化"""
		self.__list = []

	def enque(self,item):
		"""入队"""
		self.__list.append(item)
	
	def deque(self):
		"""出队"""
		return self.__list.pop(0)
	
	def is_empty(self):
		"""判断队列是否为空"""
		return self.__list == []

	def size(self):
		"""队列大小"""
		return len(self.__list)

def copy(list1):
	''''备份'''
	list2 = []
	for n in list1:
		list2.append(n)
	return list2



def print_all_pop_sequence(insequnce,stack,outsequence):

	'''打印出按顺序输入堆栈的元素的出栈可能结果'''

	# stack = Stack() #堆栈
	# insequnce = Queue() #输入队列
	# outsequence = Queue() #输出队列

	# if (not stack.is_empty()):#堆栈非空时，栈顶元素出栈，进入输出队列
	# 	outsequence.enque(stack.pop())
	# 	print_all_pop_sequence(insequnce,stack,outsequence,n)#递归

	# if (not insequnce.is_empty()):#输入队列非空时，入栈
	# 	stack_copy.push(insequnce.deque())
	# 	print_all_pop_sequence(insequnce,stack_copy,outsequence_copy,n)#递归

	if insequnce.is_empty():
		if stack.is_empty():
			'''输入队列为空，堆栈为空：输出队列输出'''
			while(not outsequence.is_empty()):

				print outsequence.deque(),
			print ""
		elif (not stack.is_empty()):
			'''输入队列为空，堆栈非空：堆栈-->输出队列'''
			outsequence.enque(stack.pop())
			#对新的情况递归处理
			print_all_pop_sequence(insequnce,stack,outsequence)

	elif (not insequnce.is_empty()):
		'''输入队列非空'''
		if (not stack.is_empty):
			'''堆栈不空：堆栈-->输出队列'''

			#产生不同分支，备份
			stack_copy = Stack()
			insequnce_copy = Queue()
			outsequence_copy = Queue()
			stack_copy = copy(stack)
			insequnce_copy = copy(insequnce)
			outsequence_copy = copy(outsequence)

			outsequence_copy.enque(stack_copy.pop())
			print_all_pop_sequence(insequnce_copy,stack_copy,outsequence_copy)

		#输入队列-->堆栈
		stack.push(insequnce.deque())
		print_all_pop_sequence(insequnce,stack,outsequence)




	

if __name__ == '__main__':

	insequnce1 = Queue()
	insequnce1.enque(1)
	insequnce1.enque(2)	
	insequnce1.enque(3)
	insequnce1.enque(4)
	# n = insequnce1.size()#输入队列的大小

	stack1 = Stack()	
	outsequence1 = Queue()

# 	count = 0
# while count < 10000:
# 	count += 1
	print_all_pop_sequence(insequnce1,stack1,outsequence1)
