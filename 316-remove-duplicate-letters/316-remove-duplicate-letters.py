class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_appear_index = {char: idx for idx, char in enumerate(s)}
        stack = []
        for i, char in enumerate(s):
            if char not in stack:
                while stack and stack[-1] > char and last_appear_index[stack[-1]] > i:
                    stack.pop()
                stack.append(char)
        return "".join(stack)