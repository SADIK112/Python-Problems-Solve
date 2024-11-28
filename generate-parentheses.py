# Solution

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []
    
        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(sol[:]))
                return

            if (openN < n):
                sol.append("(")
                backtrack(openN + 1, closeN)
                sol.pop()

            if (closeN < openN):
                sol.append(")")
                backtrack(openN, closeN + 1)
                sol.pop()

        backtrack(0, 0)
        return res


  # Time Complexity of Solution 1 - O(4n / square_root of n)
  # Space Complexity of Solution 1 - O(n)
