class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        unordered_set<int> hset;
        int result = 0,sum = 0;
        int i=0;
        for(int j=0;j<nums.size();j++) {
            //check elem in set and update
            while(hset.find(nums[j]) != hset.end()) {
                hset.erase(nums[i]);
                sum -= nums[i];
                i++;
            }
            hset.insert(nums[j]);
            sum += nums[j];
            result = max(sum,result);
        }
        return result;
    }
};