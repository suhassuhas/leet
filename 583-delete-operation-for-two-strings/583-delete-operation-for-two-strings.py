class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        s1,s2 = len(word1),len(word2)
        dp = [[0]*(s2+1) for _ in range(s1+1)]
        for i in range(s1+1):
            for j in range(s2+1):
                if i==0 or j==0:
                    continue
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        #print(dp)
        return s1+s2-(2*dp[s1][s2])