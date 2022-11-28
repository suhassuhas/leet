class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lostmap = defaultdict(int)
        for match in matches:
            lostmap[match[1]]+=1
            lostmap[match[0]]+=0
        zlost,olost = [],[]
        for los in sorted(lostmap.keys()):
            if lostmap[los] == 0:
                zlost.append(los)
            elif lostmap[los] == 1:
                olost.append(los)
        return [zlost,olost]
            