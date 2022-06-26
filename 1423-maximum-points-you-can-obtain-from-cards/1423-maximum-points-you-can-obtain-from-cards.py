class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        res = sum(cardPoints[:k])
        curr = res
        for i in range(k-1,-1,-1):
            curr -= cardPoints[i]
            curr += cardPoints[n-k+i]
            res = max(res,curr)
        return res
        