class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        mat_row = len(mat)
        mat_col = len(mat[0])

        def sortDiagonal(start_row,start_col):
            values = []
            while start_col < mat_col and start_row < mat_row:
                values.append(mat[start_row][start_col])
                start_col += 1
                start_row += 1
            values.sort()
            while start_col and start_row:
                start_col -= 1
                start_row -= 1
                mat[start_row][start_col] = values.pop()

        for row in range(mat_row): sortDiagonal(row,0)
        for col in range(mat_col): sortDiagonal(0,col)            
        return mat