class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.board = matrix

        for i in range(self.n):
            for j in range(1, self.m):
                self.board[i][j] = self.board[i][j-1] + self.board[i][j]

        for i in range(self.m):
            for j in range(1, self.n):
                self.board[j][i] = self.board[j-1][i] + self.board[j][i]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.board[row2][col2]

        if col1 - 1 >= 0:
            total -= self.board[row2][col1-1]
        
        if row1 - 1 >= 0:
            total -= self.board[row1-1][col2]
        
        if row1 -1 >= 0 and col1 - 1 >= 0:
            total += self.board[row1-1][col1-1]

        return  total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)