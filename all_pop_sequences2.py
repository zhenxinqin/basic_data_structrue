#coding=utf-8

#list实现队列：pop(0),append
#list实现堆栈：pop,append

def copy(list1):
	''''备份'''
	list2 = []
	for n in list1:
		list2.append(n)
	return list2

def pop_sequences(inline,stack,outline):
	'''按顺序入栈，输出所有出栈的可能结果'''
	if len(inline) == 0:
		if len(stack) == 0:
			'''输入队列为空，堆栈为空：输出队列输出'''
			# count = count + 1
			# while count == 5:
			for n in outline:
				print n,
			print''
			

		else: 
			'''输入队列为空，堆栈非空：出队列'''
			outline.append(stack.pop())
			#对新的情况递归处理
			pop_sequences(inline,stack,outline)

	elif len(inline) != 0:
		'''输入队列非空'''
		if (len(stack)) != 0:
			'''堆栈不空：堆栈-->输出队列'''

			#产生不同分支，备份
			inline_copy = []
			# print "inline",id(inline)
			# print "inline_copy",id(inline_copy)
			stack_copy = []
			outline_copy = []
			outline_copy = copy(outline)
			stack_copy = copy(stack)
			inline_copy = copy(inline)
			

			outline_copy.append(stack_copy.pop())
			pop_sequences(inline_copy,stack_copy,outline_copy)

		#输入队列-->堆栈
		stack.append(inline.pop(0))
		pop_sequences(inline,stack,outline)
	return count



if __name__ == '__main__':

	# inline = [1,2,3,4]#输入队列
	inline = ['a','b','c','d']#输入队列
	stack = []
	outline = []
	count = 0
	pop_sequences(inline,stack,outline)