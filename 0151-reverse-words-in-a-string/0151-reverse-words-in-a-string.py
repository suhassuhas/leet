class Solution:
    def reverseWords(self, s: str) -> str:
        # def checkempty(string):
        #     #print(string)
        #     return string != " " and string != ''
        # arr = s.split(" ")[::-1]
        # arr = list(filter(checkempty,arr))
        # return " ".join(arr)
        return " ".join(s.split()[::-1])