#coding=utf8

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
	
	def is_empety(self):
		"""判断队列是否为空"""
		return self.__list == []

	def size(self):
		"""队列大小"""
		return len(self.__list)

if __name__ == '__main__':
	queue = Queue()
	queue.enque(1)
	queue.enque(2)
	queue.enque(3)
	queue.enque(4)
	print 'size:',queue.size()
	print 'is it empety?',queue.is_empety()
	print queue.deque()
	print queue.deque()
	print queue.deque()
	print queue.deque()
	print 'is it empety?',queue.is_empety()