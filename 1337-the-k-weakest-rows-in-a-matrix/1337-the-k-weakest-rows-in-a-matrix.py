class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i in range(len(mat)):
            soldiers = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    break
                soldiers += 1
            heap.append((soldiers, i, mat[i]))
        heap.sort()
        return [x[1] for x in heap[:k]]