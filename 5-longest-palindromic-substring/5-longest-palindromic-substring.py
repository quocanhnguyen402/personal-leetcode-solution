class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(0,len(s)):
            tmp = s[i]
            left_pointer, right_pointer = i-1 ,i+1

            while left_pointer >= 0 and s[left_pointer] == s[i]:
                tmp = s[left_pointer] + tmp
                left_pointer -= 1
                

            while right_pointer < len(s) and s[right_pointer] == s[i]:
                tmp += s[right_pointer]
                right_pointer += 1

            while left_pointer >= 0 and right_pointer < len(s):
                if s[left_pointer] == s[right_pointer]:
                    tmp = s[left_pointer] + tmp + s[right_pointer]
                    left_pointer -= 1
                    right_pointer += 1
                else:
                    break
            if len(tmp) > len(result):
                result = tmp
        return result