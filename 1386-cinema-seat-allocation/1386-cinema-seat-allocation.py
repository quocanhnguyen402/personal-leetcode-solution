class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        res = 2*n
        seat_by_row = {}
        for r in reservedSeats:
            if r[0] not in seat_by_row:
                seat_by_row[r[0]] = [r[1]]
            else:
                seat_by_row[r[0]].append(r[1])

        for row in seat_by_row:
            cnt = 0
            if 2 not in seat_by_row[row] and 3 not in seat_by_row[row] and 4 not in seat_by_row[row] and 5 not in seat_by_row[row]:
                cnt +=1
            if 6 not in seat_by_row[row] and 7 not in seat_by_row[row] and 8 not in seat_by_row[row] and 9 not in seat_by_row[row]:
                cnt += 1
            if 4 not in seat_by_row[row] and 5 not in seat_by_row[row] and 6 not in seat_by_row[row] and 7 not in seat_by_row[row] and cnt == 0:
                cnt += 1
            res += (cnt-2)
        return res