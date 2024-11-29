# Solution 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        rate = high

        while low <= high:
            k = (low + high) // 2
            totalTime = 0
            
            for pile in piles:
                totalTime += math.ceil(pile / k)
            
            if totalTime <= h:
                high = k - 1
                rate = k
            else:
                low = k + 1

        return rate

# Time Complexity of Solution - O(nlogm)
# Space Complexity of Solution 1 - O(1)
