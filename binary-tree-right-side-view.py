# Solution

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        q = collections.deque([root])
        
        while q:
            rightSide = None
            qLength = len(q)

            for i in range(qLength):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                output.append(rightSide.val)

        return output

# Time Complexity of Solution  - O(n)
# Space Complexity of Solution - O(n)
