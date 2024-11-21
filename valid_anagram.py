# Solution 1:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        hashTable1 = {}
        hashTable2 = {}

        for char in s:
            hashTable1[char] = hashTable1.get(char, 0) + 1

        for char in t:
            hashTable2[char] = hashTable2.get(char, 0) + 1

        for key, value in hashTable1.items():
            if key not in hashTable2:
                return False

            charValue = hashTable2[key]

            if value != charValue:
                return False

        return True

  # Time Complexity of Solution 1 - O(n) + O(m) + O(n) = O(n  + m)
  # Space Complexity of Solution 1 - O(n + m)

# Solution 2:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        hashTable1, hashTable2 = {}, {}

        for i in range(len(s)):
            hashTable1[s[i]] = hashTable1.get(s[i], 0) + 1
            hashTable2[t[i]] = hashTable2.get(t[i], 0) + 1

        for key in hashTable1:
            if hashTable1[key] != hashTable2.get(key, 0):
                return False
        return True


# Time Complexity of Solution 1 - O(n + M)
# Space Complexity of Solution 1 - O(n + m)
