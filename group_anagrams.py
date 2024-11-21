# Solution 1:
class Solution:
    def groupAnagrams(strs):
        hashMap = {}

        for word in strs:
            sortedStr = ''.join(sorted(word))
            hashMap.setdefault(sortedStr, []).append(word)

        return list(hashMap.values())

  # Time Complexity of Solution 1 - O(m * nlongn)
  # Space Complexity of Solution 1 - O(m * n)

# Solution 2:

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1

            hashMap[tuple(count)].append(word)

        return hashMap.values()

  # Time Complexity of Solution 1 - O(m * n)
  # Space Complexity of Solution 1 - O(m * n + k)
