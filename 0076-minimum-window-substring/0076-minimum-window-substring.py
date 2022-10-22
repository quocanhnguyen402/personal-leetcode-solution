class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        else:
            counter_t = Counter(t)
            counter = {}
            for i in counter_t:
                counter[i] = 0
            min_len = float("inf")
            result = [-1,-1]
            found = 0
            needed = len(counter_t)
            right = -1
            left = 0
            while right <= len(s) - 1:
                while found != needed and right <= len(s) - 1:
                    right += 1
                    if right <= len(s) - 1:
                        char = s[right]
                        if char in counter:
                            counter[char] += 1
                            if counter[char] == counter_t[char]:
                                found += 1

                while found == needed:
                    if right - left + 1 < min_len:
                        min_len = right - left + 1
                        result[0] = left
                        result[1] = right
                    
                    char_left = s[left]
                    if char_left in counter:
                        counter[char_left] -= 1
                        if counter[char_left] < counter_t[char_left]:
                            found -= 1
                    left += 1
            
            return s[result[0]:result[1] + 1] if min_len != float("inf") else ""