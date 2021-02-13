from typing import List

from algorithms.ds import TreeNode


def traverse(self, root: TreeNode) -> List[int]:
	# 2/11/2021
	# iterative solution
	if not root:
		return []
	traversal = []
	queue = [root]
	while queue:
		next_queue = []
		for node in queue:
			traversal.append(node.val)
