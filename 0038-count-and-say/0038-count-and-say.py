class Solution:
    def countAndSay(self, n: int) -> str:
        base = "1"
        for i in range(1,n):
            count = 0
            current_char = base[0]
            new_base = ""
            for j in range(0,len(base)):
                if base[j] == current_char:
                    count += 1
                else:
                    new_base += str(count) + current_char
                    count = 1
                    current_char = base[j]
            new_base += str(count) + current_char
            base = new_base
        return base