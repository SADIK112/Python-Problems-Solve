# Solution:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashNums = {}
        
        for i in range(len(nums)):
            
            diff = target - nums[i]
            if diff not in hashNums:
                hashNums[nums[i]] = i
            else: 
                return [hashNums.get(diff), i]

# Time Complexity of Solution - O(n)
# Space Complexity of Solution- O(n)
