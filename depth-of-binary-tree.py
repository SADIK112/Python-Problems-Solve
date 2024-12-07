# Solution

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Swap the left and right children
        left = root.left
        right = root.right
        return 1 + max(self.maxDepth(left), self.maxDepth(right))

# Time Complexity of Solution 1 - O(n)
# Space Complexity of Solution 1 - O(1)
