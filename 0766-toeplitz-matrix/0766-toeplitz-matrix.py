class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row, col = len(matrix),len(matrix[0])
        for i in range(0,col-1):
            _col = i
            _row = 0
            value = matrix[_row][_col]
            while _col < col and _row < row:
                if matrix[_row][_col] != value:
                    return False
                _col += 1
                _row += 1
                
        for i in range(1,row-1):
            _col = 0
            _row = i
            value = matrix[_row][_col]
            while _col < col and _row < row:
                if matrix[_row][_col] != value:
                    return False
                _col += 1
                _row += 1
        return True