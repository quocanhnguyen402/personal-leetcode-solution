class Solution:
    def largestOverlap(self, img1 : List[List[int]], img2:  List[List[int]]):
        row, col = len(img1),len(img1[0])
        count1 = []
        count2 = []
        for i in range(row):
            for j in range(col):
                if img1[i][j] == 1:
                    count1.append([i,j])
                if img2[i][j] == 1:
                    count2.append([i,j])
        res = 0
        shift_pattern = {}

        for i in count1:
            for j in count2:
                x = i[0] - j[0]
                y = i[1] - j[1]
                shift = (x,y)
                if shift in shift_pattern:
                    shift_pattern[shift] += 1
                else:
                    shift_pattern[shift] = 1
                res = max(res,shift_pattern[shift])
        return res