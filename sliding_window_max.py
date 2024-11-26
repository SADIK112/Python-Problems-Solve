# Solution 1:

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        res = []
        maxL = float('-inf')
        while l + k <= len(nums):
            maxL = max(maxL, nums[r])
            r += 1
            if (r - l) == k:
                l += 1
                res.append(maxL)
                maxL = float('-inf')
                r = l
        return res

  # Time Complexity of Solution 1 - O(n) = O(n)
  # Space Complexity of Solution 1 - O(n)

# Solution 2:

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l, r = 0, 0

        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output


  # Time Complexity of Solution 2 - O(n) = O(n)
  # Space Complexity of Solution 2 - O(n)
