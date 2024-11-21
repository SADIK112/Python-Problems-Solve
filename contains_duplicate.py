# Solution 1:
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         numsLength = len(nums)
         numsToSet = set(nums)
         return False if len(list(numsToSet)) == numsLength else True

# Time Complexity of Solution 1 - O(n) + O(n) = O(n)
# Space Complexity of Solution 1 - O(n)


# Solution 2:
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        return False

# Time Complexity of Solution 2 - O(n) + O(n) = O(n)
# Space Complexity of Solution 2 - O(n)
