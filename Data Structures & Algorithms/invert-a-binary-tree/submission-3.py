# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # def dfs(root):
        #     if not root:
        #         return
            
        #     root.left, root.right = root.right, root.left
        #     dfs(root.left)
        #     dfs(root.right)
        
        # dfs(root)
        # return root
        #[1,2,3,4,5,6,7]
        #[[1], [2,3], [4,5,6,7]]
        # [[1], [3, 2], [7,6,5,4]]
        # skip n + 1 elem for the current root

        # implement bfs to get a queue of the elements
        if not root:
            return None
        from collections import deque

        queue = deque([root])
        while len(queue) > 0:
            for i in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)

        return root







