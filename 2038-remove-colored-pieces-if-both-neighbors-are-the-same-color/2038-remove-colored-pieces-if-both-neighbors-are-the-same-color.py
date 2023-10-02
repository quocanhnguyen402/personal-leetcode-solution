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
        
        alice_turn = True
        while True:
            if alice_turn:
                moved[0] -= 1
                if moved[0] < 0:
                    return False
            else:
                moved[1] -= 1
                if moved[1] < 0:
                    return True
            alice_turn = not alice_turn