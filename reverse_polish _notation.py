# Solution

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char in "+-*/":
                res = 0
                e1 = stack.pop()
                e2 = stack.pop()
                if char == "+":
                    res = int(e2 + e1)
                elif char == "-":
                    res = int(e2 - e1)
                elif char == "*":
                    res = int(e2 * e1)
                else:
                    res = int(e2 / e1)
                print(res)
                stack.append(res)
            else:
                stack.append(int(char))
            print(stack)
        return stack[-1] if stack else 0

  
  # Time Complexity of Solution- O(n) = O(n)
  # Space Complexity of Solution- O(n)
