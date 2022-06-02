class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n = len(matrix),len(matrix[0])
        ans = []
        for i in range(n):
            tmp = []
            for j in range(m):
                tmp.append(matrix[j][i])
            ans.append(tmp)
        return ans