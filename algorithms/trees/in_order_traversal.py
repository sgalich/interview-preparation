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
		inorder.append(node.val)
		visit(node.right)
	
	inorder = []
	visit(root)
	return inorder


# Iterative
# def traverse_i(self, root: TreeNode) -> List[int]:
# 	inorder = []
# 		stack = []
# 		cur = root
# 		while cur or stack:
# 			while cur:
# 				stack.append(cur)
# 				cur = cur.left
# 			cur = stack.pop()
# 			inorder.append(cur.val)
# 			cur = cur.right
# 		return inorder
