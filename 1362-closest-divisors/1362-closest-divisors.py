class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for a in range(math.floor(math.sqrt(num+2)),0,-1):
            #print(a)
            if (num + 1) % a == 0:
                return [a,(num+1)//a]
            if (num + 2) % a == 0:
                return [a,(num+2)//a]
        return []