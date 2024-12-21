# Solution

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(t, st):
            if not t and not st:
                return True

            if (t and not st) or (st and not t):
                return False

            if t.val != st.val:
                return False 
                
            return (sameTree(t.left, st.left) and sameTree(t.right, st.right))
                
        def has_subTree(root):
            if not root:
                return False
                
            if sameTree(root, subRoot):
                return True
            
            return (has_subTree(root.left) or has_subTree(root.right))
            
        return has_subTree(root)

# Time Complexity of Solution- O(n * m)
# Space Complexity of Solution - O(n + m)
