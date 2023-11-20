class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        current_pos = {"M": [0, 0], "P": [0, 0], "G": [0, 0]}

        current_distance = 0

        for i in range(len(garbage)):
            if i > 0:
                current_distance += travel[i - 1]

            for i_garbage in range(len(garbage[i])):
                type = garbage[i][i_garbage]
                current_pos[type][1] += 1
                current_pos[type][0] = current_distance
        res = 0
        for key, pos in current_pos.items():
            res += sum(pos)
        return res