class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        
        map = {}
        for i in range(len(changed)):
            if changed[i] not in map:
                map[changed[i]] = 1
            else:
                map[changed[i]] += 1
                
        half = len(changed) // 2
        changed.sort()
        result = []
        for i in range(len(changed)):
            val = changed[i]
            if map[val] != 0:
                map[val] -= 1
                if val * 2 in map and map[val * 2] > 0:
                    map[val*2] -= 1
                    result.append(val)

        return result if len(result) == half else []