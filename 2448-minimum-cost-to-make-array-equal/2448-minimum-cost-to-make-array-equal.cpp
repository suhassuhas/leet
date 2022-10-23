#define ECOUNT 1000002
class Solution {
long ans = 1e18;
public:
    long long minCost(vector<int>& nums, vector<int>& cost) {
        long costNums[ECOUNT]={0};
        long prefixSum[ECOUNT]={0};
        long suffixSum[ECOUNT]={0};
        long sum = 0;
        int n = nums.size();
        long i = 0, j = 0;
        for(i=0; i<n ; i++) {
            costNums[nums[i]] += cost[i];
        }
        sum = 0;
        for(i=1;i<ECOUNT;i++) {
            prefixSum[i] = prefixSum[i-1] + sum;
            sum += costNums[i];
        }
        sum = 0;
        for(i=ECOUNT-2;i>=0;i--) {
            suffixSum[i] = suffixSum[i+1] + sum;
            sum += costNums[i];
            ans = min(ans,prefixSum[i]+suffixSum[i]);
        }
        return ans;
    }
};