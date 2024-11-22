# Solution 1:

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sizes, res = [], ""

        for str in strs:
            sizes.append(len(str))

        for size in sizes:
            res += "{}".format(size)
            res += ","
        res += "#"

        for str in strs:
            res += str

        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        sizes, res, i = [], [], 0

        while s[i] != "#":
            current = ""
            while s[i] != ",":
                current += s[i]
                i += 1
            print(current)
            sizes.append(int(current))
            i += 1
        i += 1
        print(sizes, i)
        for sz in sizes:
            res.append(s[i:i+sz])
            i += sz
        return res
