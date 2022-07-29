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
            word_char = word[i]
            pattern_char = pattern[i]
            index_word = word.index(word_char)
            index_pattern = pattern.index(pattern_char)
            if index_word != index_pattern:
                return False
        return True