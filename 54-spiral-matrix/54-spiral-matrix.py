class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left, right = 0, len(matrix[0])
        top, bot = 0, len(matrix)
        self.goSpiral(matrix, left, top, right, bot, result)
        return result

    def goSpiral(self, matrix, left, top, right, bot, result):
        if not (left < right and top < bot):
            return
        # Go right
        for i in range(left,right):
            result.append(matrix[top][i])
        # Remove the row we just visit
        top += 1
        # Go down
        for i in range(top,bot):
            result.append(matrix[i][right-1])
        #Remove the column we just visit
        right -= 1

        if not (left < right and top < bot):
            return

        # Go left
        for i in range(right - 1,left-1,-1):
            result.append(matrix[bot-1][i])
        # Remove the row we just visit
        bot -= 1
        # Go up
        for i in range(bot-1,top-1,-1):
            result.append(matrix[i][left])
        # Remvoe the col
        left += 1
        
        self.goSpiral(matrix, left, top, right, bot, result)