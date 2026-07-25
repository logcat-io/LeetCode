class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        dirs = [(0,1),(0,-1),(1,0), (-1,0)]
        MARK = "#"

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            
            if not( 0<= r < n and 0 <= c < m):
                return False
            
            if board[r][c] != word[idx]:
                return False

            saved = board[r][c]
            board[r][c] = MARK
            found = False

            for dr, dc in dirs:
                if dfs(r + dr, c + dc, idx + 1):
                    found = True
                    break
            board[r][c] = saved
            return found
        
        for r in range(n):
            for c in range(m):
                if dfs(r, c, 0):
                    return True
        
        return False
        