class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = len(matrix), len(matrix[0])
        first_col_marked = False

        for i in range(0,row):
            for j in range(0,col):
                if matrix[i][j] == 0:
                    if j == 0: 
                        first_col_marked = True
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0

        for i in range(row-1, -1,-1):
            for j in range(col-1, 0,-1):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if first_col_marked:
            for i in range(0,row):
                matrix[i][0] = 0