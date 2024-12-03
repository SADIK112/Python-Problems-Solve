# Solution 1

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        # find the index to remove
        indexToRemove = length - n
        # for removing first element
        if indexToRemove == 0:
            head = head.next
            return head

        count = 0
        latest = head
        # for removing any element from other index
        while latest:
            if count == indexToRemove - 1:
                latest.next = latest.next.next
                break
            latest = latest.next
            count += 1
        return head

# Time Complexity of Solution 1 - O(n)
# Space Complexity of Solution 1 - O(1)

# Solution 2:

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next

# Time Complexity of Solution 2 - O(n)
# Space Complexity of Solution 2 - O(1)
