class TreeNode:
	
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


# Recursive
def traverse_r(self, root: TreeNode) -> List[int]:

	def visit(node: TreeNode) -> None:
		if not node:
			return None
		visit(node.left)
		visit(node.right)
		postorder.append(node.val)
		
	postorder = []
	visit(root)
	return postorder


# Iterative
# def traverse_i(self, root: TreeNode) -> List[int]:
# 	arr = []
# 	visited = []
# 	stack = [root] if root else []
# 	while stack:
# 		curr = stack[-1]
# 		found = 0 
# 		if curr.right and curr.right not in visited:
# 			stack.append(curr.right)
# 			found = 1
# 		if curr.left and curr.left not in visited:
# 			stack.append(curr.left)
# 			found = 1
# 		if found == 0:
# 			stack.pop()
# 			arr.append(curr.val)
# 			visited.append(curr)
# 	return arr
