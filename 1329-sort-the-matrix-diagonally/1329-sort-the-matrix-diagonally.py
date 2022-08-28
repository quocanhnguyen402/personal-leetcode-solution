class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        def sort(i, j):
            vals = []
            while i < m and j < n:
                vals.append(mat[i][j])
                i += 1
                j += 1
            vals.sort()
            while i and j:
                j -= 1
                i -= 1
                mat[i][j] = vals.pop()
        for i in range(m): sort(i, 0)
        for j in range(n): sort(0, j)
        return mat