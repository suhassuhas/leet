class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        seen = {}
        count = 0
        for i in range(n-k+1):
            string = s[i:i+k]
            if string not in seen:
                seen[string] = True
                count += 1
        return count == 2 ** k
                