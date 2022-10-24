class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charSet = set()
        
        def overlap(cSet,word):
            prev = set()
            for c in word:
                if c in cSet or c in prev:
                    return True
                prev.add(c)
            return False
        
        def backtrack(i):
            if i == len(arr):
                return len(charSet)
            res = 0
            if not overlap(charSet,arr[i]):
                for c in arr[i]:
                    charSet.add(c)
                res = backtrack(i+1)
                for c in arr[i]:
                    charSet.remove(c)
            return max(res,backtrack(i+1))
        
        return backtrack(0)