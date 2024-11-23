# Solution 1:

class Solution:
    def isPalindrome(self, s: str) -> bool:
      s = ''.join(char for char in s.casefold() if char.isalnum())
      rev_s = s[::-1]
      
      if s == rev_s:
          return True
      return False

# Time Complexity of Solution 1 - O(n)
# Space Complexity of Solution 1 - O(n)

# Solition 2:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = len(s) - 1

        for char in s:
            if s[p] == " ":
                p -= 1
            
            if not char.isalnum() or len(char) == 0:
                continue

            if not s[p].isalnum():
                p -= 1
            if char.lower() == s[p].lower():
                p -= 1
            else: 
                return False

        return True
        
# Time Complexity of Solution 1 - O(n)
# Space Complexity of Solution 1 - O(1)
