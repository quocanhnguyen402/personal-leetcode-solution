class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        moved = [0,0]
        for i in range(1,len(colors)-1):
            char = colors[i]
            if char == colors[i-1] and char == colors[i+1]:
                if char == 'A':
                    moved[0] += 1
                else:
                    moved[1] += 1
        
        return moved[0] - moved[1] > 0