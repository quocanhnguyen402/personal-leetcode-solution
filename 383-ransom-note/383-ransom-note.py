class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        map_magazine = {}
        for char in magazine:
            if char in map_magazine:
                map_magazine[char] += 1
            else:
                map_magazine[char] = 1
        for char in ransomNote:
            if char not in map_magazine:
                return False
            elif char in map_magazine :
                if map_magazine[char] == 0:
                    return False
                else:
                    map_magazine[char] -= 1
        return True
        