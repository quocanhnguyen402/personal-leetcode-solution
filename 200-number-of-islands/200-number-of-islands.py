class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        trace = [[1]*col for _ in range(row)]
        result = 0
        def findAdjacentLand(pos_row, pos_col, trace):
            if trace[pos_row][pos_col] == 1 and grid[pos_row][pos_col] == "1":
                trace[pos_row][pos_col] = 0
                if pos_row - 1 >= 0:
                    findAdjacentLand(pos_row-1, pos_col, trace)
                if pos_row + 1 < row:
                    findAdjacentLand(pos_row+1, pos_col, trace)
                if pos_col - 1 >= 0:
                    findAdjacentLand(pos_row, pos_col-1, trace)
                if pos_col + 1 < col:
                    findAdjacentLand(pos_row, pos_col+1, trace)
        for i in range(row):
            for j in range(col):
                if trace[i][j] == 1 and grid[i][j] == "1":
                    result += 1
                    findAdjacentLand(i, j, trace)
        return result
