# Solution

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.output = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.output = max(self.output, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.output

  
# Time Complexity of Solution- O(n)
# Space Complexity of Solution - O(n)
