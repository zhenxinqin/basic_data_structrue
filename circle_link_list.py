#coding=utf8

class Node(object):
	"""节点"""
	def __init__(self, elem):
		self.elem = elem
		self.next = None

class Single_circle_link_list(object):
	"""单向循环链表"""
	def __init__(self, node=None):
		"""初始化"""
		self._head = node
		#如果有节点，则节点指向自己
		if node:
			node.next = node

	def is_empty(self):
		"""判断链表是否为空"""
		return self._head == None

	def length(self):
		"""返回列表长度"""
		cur = self._head
		count = 1
		#当游标没有指到头结点时，移动游标
		while cur.next != self._head:
			count += 1
			cur = cur.next
		return count
		
	def travel(self):
		'''遍历列表'''
		#链表为空时
		if self.is_empty():
			print "no elem"
		#链表非空
		else:
			cur = self._head
			while cur.next != self._head:
				#当游标没有指到头结点时，移动游标
				print cur.elem,# for pre python3.x
				#print(cur.elem,end = "")# for python3.x
				cur = cur.next
			# print('\n')
			#退出循环时，指向尾节点
			print cur.elem,
			print('')
	
	def add(self,item):
		"""链表头部添加元素"""
		node = Node(item)

		#链表为空：
		if self.is_empty():
			self._head = node
			node.next = node

		#链表不为空：
		#指向尾节点的指针
		else:
			rear = self._head
			while rear.next	!= self._head:
				rear = rear.next
			#节点指向原头结点	
			node.next = self._head
			self._head = node
			#尾节点指向新头结点
			rear.next = node

	def append(self,item):
		'''链表尾部添加元素'''
		node = Node(item)
		# if self.is_empty():
		#链表为空
		if self._head == None:
			self._head = node
			node.next = node
		#链表不为空
		else:
			cur = self._head
			while cur.next != self._head:
				cur = cur.next
			#退出循环时，指针cur指向尾节点
			cur.next = node
			node.next = self._head 

	def insert(self,pos,item):
		'''在指定位置插入数据'''
		node = Node(item)
		pre = self._head

		#pos 小于1时视为前插
		if pos <= 1:
			self.add(item)
		#pos 大于链表长度视为后插
		elif pos > self.length():
			self.append(item)
		#正常情况
		else:
			while (pos-1) > 0:
				pos -= 1
				pre = pre.next
			node.next = pre.next
			pre.next = node
		
	def search(self,item):
		'''查找节点是否存在'''
		cur = self._head
		while cur.next != self._head:
			if cur.elem == item:
				print "exist"
				return 
			else:
				cur = cur.next
		#退出循环时，指针cur指向尾节点
		if cur.elem == item:
			print "exist in the rear"
		else:
			print "dont exist"
		# return 


	def remove(self,item):
		'''删除链表中的第一个特定值'''
		#链表为空
		if self.is_empty():
			return

		cur = self._head
		pre = None
		rear = self._head
		while rear.next != self._head:
			rear = rear.next

		#遍历节点,在尾节点前退出
		while cur.next != self._head:
			#不相等时，指针前移
			if cur.elem != item:
				pre = cur
				cur = cur.next
			#相等时
			else:
				if cur == self._head:#指针在头结点
					self._head = cur.next
					rear.next = self._head
				else:
					pre.next = cur.next#指针在中间节点
				return
		#退出while循环时，cur指向尾节点
		if cur.elem == item:
			if cur == self._head:
				self._head = None
			else:
				pre.next = cur.next
		else:
			print "要删除的节点不存在"


		



if __name__ == '__main__':
	node = Node(3)
	linklist1 = Single_circle_link_list(node)#初始化一个非空循环链表
	# linklist2 = Single_circle_link_list()#初始化一个空的单循环链表
	print(linklist1.is_empty())
	# print(linklist2.is_empty())
	# linklist2.add(1)#空链表前加节点,1
	# linklist2.append(3)#后加，1 3
	# linklist2.remove(1)#移除头结点，3
	# linklist2.remove(3)#移除尾节点
	# linklist2.travel()
	linklist1.add(1)#非空前加，1 3
	linklist1.insert(1,4)#在第一个位置插入4,4 1 3
	linklist1.insert(3,6)#4 1 6 3
	# linklist1.search(7)
	# linklist1.travel()
	linklist1.insert(19,5)#4 1 6 3 5
	linklist1.remove(4)#1 6 3 5
	linklist1.remove(5)
	linklist1.travel()


	


			

				
		
