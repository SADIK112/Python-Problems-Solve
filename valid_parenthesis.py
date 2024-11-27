# Solution 1:

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mirror_map = {
            '(': ')',
            '{': '}', 
            '[': ']',
        }
        for c in s:
            if c in mirror_map.keys():
                stack.append(c)
            else:
                mirrorEle = ""
                if len(stack) != 0:
                    topEle = stack[len(stack) - 1]
                    mirrorEle = mirror_map[topEle]
                
                if c != mirrorEle:
                    return False
                
                stack.pop()
        return True if not stack else False


# Time Complexity of Solution 1 - O(n)
# Space Complexity of Solution 1 - O(n)

# Solution 2:

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mirror_map = {
            ')': '(',
            '}': '{', 
            ']': '[',
        }
        for c in s:
            if c in mirror_map:
                if stack and stack[-1] == mirror_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                    
        return True if not stack else False

# Time Complexity of Solution 1 - O(n)
# Space Complexity of Solution 1 - O(n)
                
