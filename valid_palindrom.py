# Solution 1:

class Solution:
    def isPalindrome(self, s: str) -> bool:
      s = ''.join(char for char in s.casefold() if char.isalnum())
      rev_s = s[::-1]
      
      if s == rev_s:
          return True
      return False

def isPalindrome(s):
    p = len(s) - 1

    for char in s:
        print("char", char)
        print("last", s[p])
        
        if not char.isalnum():
            continue
        
        if not s[p].isalnum():
            p -= 1
        print("---")
        if char.lower() == s[p].lower():
            p -= 1
        else: 
            return False

    return True
        
    
