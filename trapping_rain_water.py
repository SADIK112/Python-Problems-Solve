# Solution 1:

class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        current_left_max = 0
        current_right_max = 0
        _sum = 0
        
        for i in range(1, len(height)):
            current_left_max = max(current_left_max, height[i - 1])
            max_left[i] = current_left_max

        for j in range(len(height) - 2, -1, -1):
            current_right_max = max(current_right_max, height[j + 1])
            max_right[j] = current_right_max

        for k in range(len(height)):
            _min = min(max_left[k], max_right[k])
            unit = _min - height[k]
            if unit > 0:
                _sum += unit

        return _sum


# Time Complexity of Solution 1 - O(n) + O(n) + O(n) = O(n)
# Space Complexity of Solution 1 - O(n)

# Solution 2:
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                diff = maxL - height[l]
                res += diff
            else:
                r -= 1
                maxR = max(maxR, height[r])
                diff = maxR - height[r]
                res += diff
        return res

# Time Complexity of Solution 1 - O(n)
# Space Complexity of Solution 1 - O(1)
