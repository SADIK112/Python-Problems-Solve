# Solution 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): 
            return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        need, have = len(countT), 0
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            print(c)
            window[c] = window.get(c, 0) + 1

            if c in t and countT[c] == window[c]:
                have += 1
            while have == need:
                res = [l, r]
                resLen = (l - r) + 1
                # pop element from the window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""


  # Time Complexity of Solution 1 - O(n) = O(n)
  # Space Complexity of Solution 1 - O(n)
