class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0, r = numbers.size() -1;
        int sumlr = 0;
        while (l < r) {
            sumlr = numbers[l] + numbers[r];
            if (sumlr == target) {
                return  vector<int>{l+1,r+1};
            } else if (sumlr>target) {
                r--;
            } else {
                l++;
            }
        }
        return vector<int>{};
    }
};