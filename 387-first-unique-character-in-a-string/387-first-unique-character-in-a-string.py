class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        for i in range(0,len(s)):
            char = s[i]
            if char not in map:
                map[char] = i
            else:
                map[char] = -1
        for key in map:
            if map[key] != -1:
                return map[key]
        return -1