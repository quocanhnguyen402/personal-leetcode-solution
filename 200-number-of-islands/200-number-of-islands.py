class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        result = 0
        def findAdjacentLand(pos_row, pos_col):
            if grid[pos_row][pos_col] == "1":
                grid[pos_row][pos_col] = "-1"
                if pos_row - 1 >= 0:
                    findAdjacentLand(pos_row-1, pos_col)
                if pos_row + 1 < row:
                    findAdjacentLand(pos_row+1, pos_col)
                if pos_col - 1 >= 0:
                    findAdjacentLand(pos_row, pos_col-1)
                if pos_col + 1 < col:
                    findAdjacentLand(pos_row, pos_col+1)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    result += 1
                    findAdjacentLand(i, j)
        return result
