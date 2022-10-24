class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        n = len(startTime)
        ans = 0
        for i in range(n):
            sT = startTime[i]
            eT = endTime[i]
            if queryTime>=sT and queryTime <=eT:
                ans+=1
        return ans