class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for char in s:
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1
        
        freq = dict(sorted(freq.items(), key=lambda x:x[1],reverse=True))
        out = ""
        for key in freq:
            out += "".join(key*freq[key])
        return out
            