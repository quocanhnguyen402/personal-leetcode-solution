class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visited = set()
        
        # To prevent TLE,reverse the word if frequency of the first letter is more than the last letter's
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        
        def dfs(i,j,count):
            if count == len(word):
                return True
            if i < 0 or i >= row or j < 0 or j >= col:
                return False
            if (i,j) in visited:
                return False
            if board[i][j] != word[count]:
                return False
            visited.add((i,j))
            up = dfs(i - 1, j, count + 1)
            down = dfs(i + 1, j, count + 1)
            left = dfs(i, j - 1, count + 1)
            right = dfs(i, j + 1, count + 1)
            visited.remove((i,j))
            return (up or down or left or right)
        
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if dfs(i,j,0):
                    return True
        return False
        