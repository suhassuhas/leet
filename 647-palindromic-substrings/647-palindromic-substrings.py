class Solution:
    def countSubstrings(self, string: str) -> int:
        n=len(string)
        count=0
        for i in range(n):
            j=0
            while i+j<n and i-j>=0:
                if(string[i+j]!=string[i-j]):
                    break
                else:
                    count+=1
                j+=1
        for i in range(n):
            j=0
            while i+j+1<n and i-j>=0:
                if(string[i+j+1]!=string[i-j]):
                    break
                else:
                    count+=1
                j+=1
        return count