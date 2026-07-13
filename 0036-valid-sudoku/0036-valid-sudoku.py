from collections import defaultdict

class Solution:
    def check_row(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = board[i]
            t = "".join(row).replace(".","")
            if len(t) != len(set(t)):
                return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.check_row(board):
            return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                check = defaultdict(int)
                for k in range(3):
                    for w in range(3):
                        cell = board[k+i][w+j]
                        if cell == ".": continue
                        if cell in check:
                            return False
                        check[cell] = 1
        
        for i in range(9):
            for j in range(i+1, 9):
                board[i][j], board[j][i] = board[j][i], board[i][j]
        
        if not self.check_row(board):
            return False
        
        return True
