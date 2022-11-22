class Solution:
    def numSquares(self, n: int) -> int:
        dp=[1000]*(n+1)
        m=int(math.sqrt(n))
        for i in range(1,n+1):
            for j in range(1,m+1):
                if i==j*j:
                    dp[i]=1
                elif i>j*j:
                    dp[i] = min(dp[i],dp[i-j*j]+1)
        #print(dp)
        return dp[n]