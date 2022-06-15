class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        words.sort(key=len)
        result = 1
        for w in words:
            dp[w] = 1
            for i in range(len(w)):
                prev = w[:i]+w[i+1:]
                if prev in dp:
                    dp[w] = max(dp[w],dp[prev]+1)
                    result = max(dp[w],result)
        return result