#coding=utf-8

class Node():
	"""docstring for node"""
	def __init__(self, item):
		self.elem = item
		self.lchild = None
		self.rchild = None


class BinTree():
	"""docstring for BinTree"""
	def __init__(self):

		self.root = None

	def add(self,item):
		'''往二叉树中添加节点'''
		node = Node(item)
		if self.root is None:
			self.root = node
			return
	
		queue = [self.root]
		while queue:
			#队列不空时寻找可以插入节点的地方
			cur_node = queue.pop(0)
			if cur_node.lchild is None:
				cur_node.lchild = node
				return
			else:
				queue.append(cur_node.lchild)
			
			if cur_node.rchild is None:
				cur_node.rchild = node
				return
			else:	
			
				queue.append(cur_node.rchild)
		

	def breath_travel(self):
		'''树的广度遍历'''
		if self.root is None:
			return
		queue = [self.root]

		while queue:

			cur_node = queue.pop(0)
			print cur_node.elem,
			if cur_node.lchild is not None:
				# print cur_node.lchild.elem,
				queue.append(cur_node.lchild)
			if cur_node.rchild is not None:
				# print cur_node.rchild.elem,
				queue.append(cur_node.rchild)

	def pre_travel(self,node):
		'''
		先序遍历
		node：根节点
		'''
		if node is None:
			return
		
		print node.elem,
		self.pre_travel(node.lchild)
		self.pre_travel(node.rchild)

	def in_order(self,node):
		'''
		中序遍历
		node：根节点
		'''
		if node is None:
			return
		self.in_order(node.lchild)
		print node.elem,
		self.in_order(node.rchild)

	def post_order(self,node):
		'''
		后序遍历
		node：根节点
		'''
		if node is None:
			return
		self.post_order(node.lchild)
		print node.elem,
		self.post_order(node.rchild)
	
 
		

if __name__ == '__main__':
	tree = BinTree()
	tree.add(1)
	tree.add(2)
	tree.add(3)
	tree.add(4)
	tree.add(5)
	tree.add(6)
	tree.add(7)
	tree.add(8)
	tree.add(9)
	# import pdb;pdb.set_trace()
	tree.breath_travel()
	print''
	tree.pre_travel(tree.root)
	print''
	tree.in_order(tree.root)

