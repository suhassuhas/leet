class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m,n = len(matrix),len(matrix[0])
        self.rowMatrix = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j !=0:
                    self.rowMatrix[i][j] = self.rowMatrix[i][j-1] + matrix[i][j]
                else:
                    self.rowMatrix[i][j] = matrix[i][j]
        print(self.rowMatrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1,row2+1):
            total +=self.rowMatrix[i][col2] -(self.rowMatrix[i][col1-1] if col1 != 0 else 0)
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)