class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.board = [[0 for _ in range(self.m+1)] for _ in range(self.n+1)]

        for i in range(self.n):
            rowP = 0
            for j in range(self.m):
                rowP += matrix[i][j]
                self.board[i+1][j+1] = self.board[i][j+1] + rowP

        for r in self.board:
            print(*r)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.board[row2+1][col2+1]
        total -= self.board[row1][col2+1]
        total -= self.board[row2+1][col1]
        total += self.board[row1][col1]

        return  total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)