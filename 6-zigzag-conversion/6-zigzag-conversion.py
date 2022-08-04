class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = [""]*numRows
        index = 0
        while index < len(s):
            # A block of zig zag numRows = 4 have the length of 2*numRows-2 = 6
            #           distance to the same row
            # @0          6 but index 6 is not in the block
            # @1   @5     4
            # @2 @4       2
            # @3          0
            result[0] += s[index]
            row = 1
            while 2*numRows-2 - 2*row >= 0:
                first_index = index + row
                second_index = index + row + 2*numRows-2 - 2*row

                if first_index != second_index:
                    if first_index < len(s):
                        result[row] += s[first_index]
                    if second_index < len(s):
                        result[row] += s[second_index]
                else:
                    if first_index < len(s):
                        result[row] += s[first_index]
                row += 1
            index += 2*numRows-2

        return "".join(result)
        