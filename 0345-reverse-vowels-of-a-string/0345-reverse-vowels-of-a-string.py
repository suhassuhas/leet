class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        i,j = 0,n-1
        string = s
        vowel = "aeiouAEIOU"
        while i<j:
            if s[i] in vowel and s[j] in vowel:
                string = string[:i] +s[j] + string[i+1:]
                string = string[:j] +s[i] + string[j+1:]
                i+=1
                j-=1
            if s[i] not in vowel:
                i+=1
            if s[j] not in vowel:
                j-=1
        return string