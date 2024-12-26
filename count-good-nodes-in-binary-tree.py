# Solution - DFS

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):
            if not node:
                return 0
            
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        
        return dfs(root, root.val)

# Time Complexity of Solution- O(n)
# Space Complexity of Solution - O(n)

# Solution - BFS

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        q = collections.deque()

        q.append((root, -float('inf')))

        while q:
            node, maxVal = q.popleft()
            
            if node.val >= maxVal:
                count += 1

            if node.left:
                q.append((node.left, max(maxVal, node.val)))

            if node.right:
                q.append((node.right, max(maxVal, node.val)))

        return count

# Time Complexity of Solution- O(n)
# Space Complexity of Solution - O(n)
