class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        result = []
        for char in words:
            if self.match(char,pattern):
                result.append(char)
        return result

    def match(self,word,pattern):
        if len(word) != len(pattern):
            return False
        for i in range(0,len(word)):
            if word.index(word[i]) != pattern.index(pattern[i]):
                return False
        return True