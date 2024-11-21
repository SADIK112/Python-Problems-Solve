class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         numsLength = len(nums)
         numsToSet = set(nums)
         return False if len(list(numsToSet)) == numsLength else True
