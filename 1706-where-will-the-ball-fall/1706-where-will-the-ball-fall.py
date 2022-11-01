class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid),len(grid[0])
        ans = [-1]*n
        def dfs(row,col):
            if row == m:
                return col
            nextCol = col + grid[row][col]
            if nextCol<0 or nextCol>n-1 or grid[row][col] != grid[row][nextCol]:
                return -1
            return dfs(row+1,nextCol)
        for i in range(n):
            ans[i] = dfs(0,i)
        return ans