class Solution:
    def countLessOrEqual(self,matrix,x):
        n = len(matrix)
        count = 0
        count_in_row = n - 1
        for r in range(n):
            while count_in_row >= 0 and matrix[r][count_in_row] > x: 
                count_in_row -= 1 
            count += (count_in_row + 1)
        return count

    def kthSmallest(self, matrix, k):
        left, right = matrix[0][0], matrix[-1][-1]
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if self.countLessOrEqual(matrix,mid) >= k:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result
