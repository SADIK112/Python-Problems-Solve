# Solution 

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # second part of the linked list
        second = slow.next
        #reverse the second list
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge the list
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first,second = temp1, temp2

# Time Complexity of Solution - O(n)
# Space Complexity of Solution - O(1)
