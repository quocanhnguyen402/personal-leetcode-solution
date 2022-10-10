import string

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        length = len(palindrome)
        if length == 1:
            return ""
        else:
            mid = length // 2
            can_replace = False
            for j in range(0,mid):
                if palindrome[j] > 'a':
                    return palindrome[:j] + 'a' + palindrome[j + 1:]
            if not can_replace:
                return palindrome[:length-1] + 'b'
