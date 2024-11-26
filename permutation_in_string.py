# Solution 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0

        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
                
            indexToRemove = ord(s2[l]) - ord("a")
            indexToAdd = ord(s2[r]) - ord("a")

            s2Count[indexToAdd] += 1

            if s1Count[indexToAdd] == s2Count[indexToAdd]:
                matches += 1
            elif s1Count[indexToAdd] + 1 == s2Count[indexToAdd]:
                matches -= 1

            s2Count[indexToRemove] -= 1
    
            if s1Count[indexToRemove] == s2Count[indexToRemove]:
                matches += 1
            elif s1Count[indexToRemove] - 1 == s2Count[indexToRemove]:
                matches -= 1

            l += 1

        return matches == 26

  # Time Complexity of Solution 1 - O(n) = O(n)
  # Space Complexity of Solution 1 - O(n)
