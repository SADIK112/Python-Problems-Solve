# Solution 1:
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         numsLength = len(nums)
         numsToSet = set(nums)
         return False if len(list(numsToSet)) == numsLength else True


# Solution 2:
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        return False
