class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        moved = [0,0]
        for i in range(len(colors)):
            char = colors[i]
            if i - 1 >= 0 and i + 1 < len(colors) and char == colors[i-1] and char == colors[i+1]:
                if char == 'A':
                    moved[0] += 1
                else:
                    moved[1] += 1
        
        return moved[0] - moved[1] > 0