# Solution

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        current = dummy
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            _sum = val1 + val2 + carry
            carry = _sum // 10
            result_digit = _sum % 10
            current.next = ListNode(result_digit)
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next

# Time Complexity of Solution 1 - O(n)
# Space Complexity of Solution 1 - O(1)
