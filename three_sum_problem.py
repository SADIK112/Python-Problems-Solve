# Solution

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            L, R = i + 1, len(nums) - 1
            while L < R:
                _sum = nums[i] + nums[L] + nums[R]
                if _sum > 0:
                    R -= 1
                elif _sum < 0:
                    L += 1
                else: 
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1

        return res

# Time Complexity of Solution - O(nlong) + O(n^2) = O(n^2)
# Space Complexity of Solution - O(n)
