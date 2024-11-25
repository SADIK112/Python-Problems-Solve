# Soltution 1:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            char_set = set()
            for j in range(i, len(s)):
                if s[j] in char_set:
                    break
                char_set.add(s[j])
            res = max(res, len(char_set))

        return res

# Time Complexity of Solution 2 - O(n * n) = O(n ^ 2)
# Space Complexity of Solution 2 - O(n)

# Solution 2

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l, res = 0, 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)
        return res


# Time Complexity of Solution 2 - O(n) = O(n)
# Space Complexity of Solution 2 - O(n)
