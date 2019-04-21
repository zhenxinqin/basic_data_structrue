#coding=utf-8
'''
列表实现二叉树
'''

def bin_tree(data,left=None,right=None):
	'''
	生成二叉树
	'''
	return [data,left,right]

def is_empty(btree):
	return btree is None

def left(btree):
	return btree[1]
	
def right(btree):
	return btree[2]
	
def root(btree):
	return btree[0]

def set_root(btree,data):
	btree[0] = data

def set_left(btree,data):
	btree[1] = data

def set_right(btree,data):
	btree[2] = data

def travel(btree):
	'''
	'''
	for i in range(3):

		if btree[i] is None:
			print btree[i],
			continue
		else:
			if len(btree[i]) == 1:
				print btree[i],
			else:
				travel(btree[i])

def level_travel(btree):
	'''
	层次遍历
	'''

	out = []
	next_level =[]
	left_tree = []
	right_tree = []
	next_tree = []
	
	out.append(btree[0])
	next_level.append(btree[1])
	next_level.append(btree[2])

	while len(next_level) != 0:
	
		# left_tree = next_level.pop(0)
		# right_tree = next_level.pop(0)
		
		# if left_tree is None:
		# 	out.append(left_tree)
		# else:
		# 	level_travel(left_tree)

		# if right_tree is None:
		# 	out.append(right_tree)
		# else:
		# 	level_travel(right_tree)

		next_tree = next_level.pop(0)
		if next_tree is None:
			out.append(next_tree)
		else:
			out.append(next_tree[0])
			next_level.append(next_tree[1])
			next_level.append(next_tree[2])

	for n in out:
		print n,



		
	



	

if __name__ == '__main__':

	bt = bin_tree('1')
	set_left(bt,bin_tree('2'))
	set_right(bt,bin_tree('3'))
	set_left(left(bt),bin_tree('4'))
	set_right(left(bt),bin_tree('5'))
	set_left(left(left(bt)),bin_tree('8'))
	travel(bt)
	print''
	level_travel(bt)
	print ''
	print bt



