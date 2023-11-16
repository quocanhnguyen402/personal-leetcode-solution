class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        _set = set(nums)

        def findBinary(string: str, n: int):
            if len(string) == n:
                if string not in _set:
                    return string
                else:
                    return None
            else:
                a = findBinary(string + "0", n)
                if (a):
                    return a
                b = findBinary(string + "1", n)
                if (b):
                    return b

        return findBinary("", len(nums))