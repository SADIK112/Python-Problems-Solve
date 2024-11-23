# Solution 1:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        hashSet = set(nums)
        res = []
        count = 1
        for i in range(len(nums)):
            left_neighbor = nums[i] - 1
            right_neighbor = nums[i] + 1

            if left_neighbor in hashSet:
                continue
            else:
                if right_neighbor not in hashSet:
                    res.append(count)
                    count = 1
                while right_neighbor in hashSet:
                    if right_neighbor in hashSet:
                        count += 1
                    right_neighbor += 1
                res.append(count)
                count = 1

        return max(res)

  # Time Complexity of Solution 1 - O(n)
  # Space Complexity of Solution 1 - O(n)

# Solution 2:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      if len(nums) == 0:
        return 0
      
      numSet = set(nums)
      longest = 0
  
      for n in nums:
          if (n - 1) not in numSet:
              length = 0
              while (n + length) in numSet:
                  length += 1
              longest = max(length, longest)
      return longest

 # Time Complexity of Solution 1 - O(n)
 # Space Complexity of Solution 1 - O(n)
