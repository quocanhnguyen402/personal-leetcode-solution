class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_so_far = 0
        max_len = 0
        char = []
        for i in range(len(s)):
            char_i = s[i]
            if char_i not in char:
                char.append(char_i)
                len_so_far += 1
            else:
                index = i - 1
                char = [s[i]]
                while index >= 0 and s[index] != s[i]:
                    char.append(s[index])
                    index -= 1
                len_so_far = len(char)
            max_len = max(len_so_far,max_len)
        return max_len