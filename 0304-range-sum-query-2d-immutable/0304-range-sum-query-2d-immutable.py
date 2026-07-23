class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix[0])
        self.n = len(matrix)

        self.sum_array = [[0] * (self.m+1) for _ in range(self.n+1)]

        for i in range(self.n):
            row_cummulate = 0
            for j in range(self.m):
                row_cummulate += matrix[i][j]
                self.sum_array[i+1][j+1] = self.sum_array[i][j+1] + row_cummulate

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.sum_array[row2+1][col2+1]
        total -= self.sum_array[row2+1][col1]
        total -= self.sum_array[row1][col2+1]
        total += self.sum_array[row1][col1]
        return  total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)