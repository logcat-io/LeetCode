class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n = len(board)
        m = len(board[0])
        temp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                live_n = 0
                if i - 1 >= 0 and j - 1 >= 0 and board[i-1][j-1] == 1:
                    live_n += 1
                
                if i - 1 >= 0 and board[i-1][j] == 1:
                    live_n += 1

                if i - 1 >= 0 and j + 1 < m and board[i-1][j+1] == 1:
                    live_n += 1
                
                if j + 1 < m and board[i][j+1] == 1:
                    live_n += 1

                if i + 1 < n and j + 1 < m and board[i+1][j+1] == 1:
                    live_n += 1
                
                if i + 1 < n and board[i+1][j] == 1:
                    live_n += 1
                
                if i + 1 < n and j - 1 >=0 and board[i+1][j-1] == 1:
                    live_n += 1
                
                if j - 1 >= 0 and board[i][j-1] == 1:
                    live_n += 1

                if board[i][j] == 1 and 2 <= live_n <= 3:
                    temp[i][j] = 1
                
                if board[i][j] == 0 and live_n == 3:
                    temp[i][j] = 1
        
        for i in range(n):
            for j in range(m):
                board[i][j] = temp[i][j]


        