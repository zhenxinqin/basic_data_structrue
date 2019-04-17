#coding:utf-8

class Node(object):
	"""docstring for Node"""
	def __init__(self, element):

		self.value = element
		self.pre = None
		self.next = None

class Double_link_list(object):
	"""docstring for Double_link_list"""
	def __init__(self,node = None):
		'''
		初始化
		'''
		self.__head = node

	def is_empty(self):
		"""判断链表是否为空"""
		return self.__head == None

	def length(self):
		"""返回列表长度"""
		cur = self.__head
		count = 0
		while cur != None:
			count += 1
			cur = cur.next
		return count
		
	def travel(self):
		'''遍历列表'''
	
		cur = self.__head
		while cur is not None:
				print cur.value,
				cur = cur.next
		print('')

	def add(self,element):
		'''
		链表头部添加元素
		'''
		node = Node(element)
		node.next = self.__head
		self.__head.pre = node
		self.__head = node

	def append(self,value):
		'''
		后插元素
		'''
		node = Node(value)

		if self.__head is None:
			self.__head = node
		else:
			cur = self.__head
			while cur.next != None:
				cur = cur.next
			cur.next = node
			node.pre = cur

	def insert(self,postion,value):
		'''
		插入一个元素到双向链表
		postion：插入位置
		value：元素的值
		'''
		
		if postion <= 0:
			self.add(value)
		elif postion > self.length():
			self.append(value)

		else:
			count = 1
			node = Node(value)
			cur = self.__head
			while count != postion:
				cur = cur.next
				count += 1
			#退出时，cur指针指向插入位置的后一个元素
			node.next = cur
			node.pre = cur.pre
			cur.pre.next = node
			cur.pre = node

	def remove(self,value):

		'''
		删除链表中值为value的节点
		version1：没有考虑特殊情况,不能删除头结点和尾节点,不能删除空链表
		'''
		cur = self.__head
		while cur.next != None and cur.value != value:
			cur = cur.next
		#退出时，要删除的节点不存在：
		if cur.next is None:
			print 'dont exist'
			return
		#找到要删除的节点
		else:
			cur.pre.next = cur.next
			cur.next.pre = cur.pre
	
		
			
if __name__ == '__main__':
	dll = Double_link_list()
	print dll.travel() #打印空链表
	# dll.remove(1)
	dll.append(2) #2
	dll.add(1) #1 2
	dll.add(2) #2 1 2
	dll.add(3) #3 2 1 2
	dll.append(4) # 3 2 1 2 4
	dll.insert(3,9) #3 2 9 1 2 4
	dll.insert(-10,7)# 7 3 2 9 1 2 4
	dll.insert(18,5)# 7 3 2 9 1 2 4 5
	dll.remove(1)# 7 3 2 9 2 4 5
	dll.remove(6)
	print dll.length()
	print dll.travel()
