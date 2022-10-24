class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = [0]
        def build(index, current):
            if index == len(arr):
                res[0] = max(res[0],len(current))
            else:
                string = arr[index]
                tmp_current = current
                # Check if the string can be taken
                can_take = True
                for i in range(len(string)):
                    if string[i] in tmp_current:
                        can_take = False
                        break
                    tmp_current += string[i]
                # Take the string
                if can_take:
                    build(index + 1, current + string)
                # Dont take the string
                build(index + 1, current)
        build(0,"")
        return res[0]   