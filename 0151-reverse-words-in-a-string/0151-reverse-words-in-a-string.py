class Solution:
    def reverseWords(self, s: str) -> str:
        def checkempty(string):
            #print(string)
            return string != " " and string != ''
        arr = s.split(" ")
        arr = arr[::-1]
        arr = list(filter(checkempty,arr))
        print(arr)
        return " ".join(arr)