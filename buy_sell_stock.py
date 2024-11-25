# Solution 1:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        l, r = 0, len(prices) - 1
        maxL = 0
        while l < r:
            while r != l:
                diff = prices[r] - prices[l]
                maxL = max(maxL, diff)
                r -= 1
            l += 1
            r = len(prices) - 1
        return maxL

# Time Complexity of Solution 1 - O(n * n) = O(n ^ 2)
# Space Complexity of Solution 1 - O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        l, r = 0, 1
        maxL = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                maxL = max(maxL, diff)
            else:
                l = r
            r += 1
        return maxL

# Time Complexity of Solution 1 - O(n) = O(n ^ 2)
# Space Complexity of Solution 1 - O(1)
        
