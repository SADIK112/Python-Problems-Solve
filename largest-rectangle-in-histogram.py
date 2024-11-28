# Solution 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        length = len(heights)

        for i, e in enumerate(heights):
            j = i

            while stack and e < stack[-1][1]:
                idx, h = stack.pop()
                area = h * (i - idx)
                maxArea = max(maxArea, area)
                j = idx

            stack.append([j, e])

        while len(stack) > 0:
            idx, h = stack.pop()
            area = h * (length - idx)
            maxArea = max(maxArea, area)

        return maxArea

  # Time Complexity of Solution - O(n)
  # Space Complexity of Solution - O(n)
