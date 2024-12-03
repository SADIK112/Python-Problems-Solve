# Solution

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

# Time Complexity of Solution 1 - O(n)
# Space Complexity of Solution 1 - O(1)
        
