# Solution 1

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        container = 0
        for i in range(len(heights)):
            if i == len(heights) - 1:
                break
            r = i + 1
            while r < len(heights):
                _min = min(heights[i], heights[r])
                area = _min * (r - i)
                container = max(container, area)
                r += 1

        return container


# Time Complexity of Solution 1 - O(n * n) = O(n ^ 2)
# Space Complexity of Solution 1 - O(n)
