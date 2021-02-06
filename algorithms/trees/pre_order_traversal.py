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
		preorder.append(node.val)
		visit(node.left)
		visit(node.right)

	preorder = []
	traverse(root)
	return preorder


# Iterative
# def traverse_i(self, root: TreeNode) -> List[int]:
# 	preorder = []
# 	stack = [[root, False]]
# 	while stack:
# 		node, visited = stack.pop()
# 		if not node:
# 			continue
# 		if visited:
# 			preorder.append(node)
# 		else:
# 			stack.append([node.right, False])
# 			stack.append([node.left, False])
# 			stack.append([node.val, True])
# 	return preorder
