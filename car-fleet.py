# Solution

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [[p, s] for p, s in zip(position, speed)]

        for p, s in sorted(pair)[::-1]:
            time = (target - p) / s
            stack.append(time)
            
            while len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

# Time Complexity of Solution - O(n)
# Space Complexity of Solution - O(n)
