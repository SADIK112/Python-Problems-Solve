# Solution 1

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []

        def dfs(root, depth):
            if not root:
                return None

            if len(output) == depth:
                output.append([])

            output[depth].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        dfs(root, 0)
        return output

# Time Complexity of Solution 1 - O(n)
# Space Complexity of Solution 1 - O(n)

# Solution 2:

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                result.append(level)

        return result

# Time Complexity of Solution 1 - O(n)
# Space Complexity of Solution 1 - O(n)
