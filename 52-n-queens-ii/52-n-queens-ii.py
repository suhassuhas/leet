class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posDiag = set() # r+c
        negDiag = set() # r-c
        
        def backtrack(r):
            if r == n:
                return 1
            soln = 0
            for c in range(n):
                if c in cols or r+c in posDiag or r-c in negDiag:
                    continue
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                soln += backtrack(r+1)
                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
            return soln
        return backtrack(0)