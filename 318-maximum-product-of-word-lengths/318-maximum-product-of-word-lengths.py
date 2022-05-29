class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        values = [0] * n
        for i in range(n):
            for char in words[i]:
                values[i] |= (1<<(ord(char)-97))
        max_value = 0
        for i in range(n):
            for j in range(i+1,n):
                if values[i] & values[j] == 0:
                    max_value = max(max_value,len(words[i])*len(words[j]))
        return max_value