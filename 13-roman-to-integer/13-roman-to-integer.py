class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        subtract = {"V": "I",
               "X": "I",
               "L": "X", 
               "C": "X", 
               "D": "C", 
               "M": "C"}

        result = 0
        queue = []
        for char in s:
            if len(queue) > 0 and char in subtract and subtract[char] == queue[-1]:
                result -= map[queue[-1]]*2

            queue.append(char)
            result += map[char]
        return result