import string

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = list(string.ascii_lowercase)
        map = {}
        for i in range(0,len(alphabet)):
            map[alphabet[i]] = morse[i]

        a = []
        for i in range(0,len(words)):
            convert = ""
            for char in words[i]:
                convert += map[char]
            if convert not in a:
                a.append(convert)
        return len(a)