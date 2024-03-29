class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        moved = [0,0]
        for i in range(1,len(colors)-1):
            if colors[i] == colors[i-1] == colors[i+1]:
                if colors[i] == 'A':
                    moved[0] += 1
                else:
                    moved[1] += 1
        return moved[0] - moved[1] > 0