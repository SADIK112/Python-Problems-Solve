# Solution 

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(list1, list2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        head = dummy

        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return dummy.next

# Time Complexity of Solution 2 - O(nlogn)
# Space Complexity of Solution 2 - O(n)
