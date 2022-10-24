class Solution {
public:
    int busyStudent(vector<int>& startTime, vector<int>& endTime, int queryTime) {
        int n = startTime.size();
        int ans = 0;
        int sT,eT;
        for (int i = 0;i < n; i++) {
            sT = startTime[i];
            eT = endTime[i];
            if (queryTime >= sT && queryTime <= eT) {
                ans++;
            }
        }
        return ans;
    }
};
/***
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
***/