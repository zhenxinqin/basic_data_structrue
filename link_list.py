#coding=utf8

class Node(object):
	"""节点"""
	def __init__(self, element):
		self.element = element
		self.next = None

class Single_link_list(object):
	"""单链表"""
	def __init__(self, node=None):
		"""初始化"""
		self._head = node

	def is_empty(self):
		"""判断链表是否为空"""
		return self._head == None

	def length(self):
		"""返回列表长度"""
		cur = self._head
		count = 0
		while cur != None:
			count += 1
			cur = cur.next
		print('length:',count)
		
	def travel(self):
		'''遍历列表'''
		cur = self._head
		while cur != None:
			print cur.element,# for pre python3.x
			#print(cur.element,end = "")# for python3.x
			cur = cur.next
		# print('\n')
		print('')
	
	def add(self,item):
		"""链表头部添加元素"""
		node = Node(item)
		node.next = self._head
		self._head = node

	def append(self,item):
		'''链表尾部添加元素'''
		node = Node(item)
		# if self.is_empty():
		if self._head == None:
			self._head = node
		else:
			cur = self._head
			while cur.next != None:
				cur = cur.next
			cur.next = node 

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
		while cur != None:
			if cur.element == item:
				print "exist"
				return True
			else:
				cur = cur.next
		print "dont exist"
		return False


	def remove(self,item):
		'''删除链表中的第一个特定值'''
		cur = self._head
		pre = None
		while cur != None:
			if cur.element != item:
				pre = cur
				cur = cur.next
			else:
				if cur == self._head:#链表只有一个节点
					self._head = cur.next
				else:
					pre.next = cur.next#链表有两个以上节点
				break

		



if __name__ == '__main__':
	linklist1 = Single_link_list()
	print(linklist1.is_empty())
	linklist1.append(1)
	linklist1.remove(1)
	linklist1.is_empty()#True:成功去掉只有一个节点的链表的唯一节点，即头结点
	linklist1.add(1)
	linklist1.append(2)
	linklist1.append(3)
	linklist1.add(9)#9 1 2 3
	linklist1.append(4)
	linklist1.append(5)#9 1 2 3 4 5
	linklist1.travel() 
	linklist1.insert(3,8)# 9 1 2 8 3 4 5 
	linklist1.insert(-5,12)# 12 9 1 2 8 3 4 5 
	# linklist1.length()
	linklist1.travel()
	linklist1.insert(20,13)#12 9 1 2 8 3 4 5 13
	linklist1.remove(13)#尾节点
	linklist1.travel()
	linklist1.search(2)
	linklist1.remove(2)#middle
	linklist1.search(2)
	linklist1.travel()




			

				
		
