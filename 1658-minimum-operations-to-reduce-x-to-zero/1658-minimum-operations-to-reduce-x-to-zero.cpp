class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int l = 0 , r = 0;
        int rollsum = 0 , currsum = 0;
        int size = nums.size();
        int maxlen = 0;
        for(int i = 0; i < size; i++) {
            rollsum += nums[i];
        } 
        
        rollsum -= x;
        if(rollsum == 0) {
            return size;
        }
        
        for (r=0;r<size;r++) {
            currsum += nums[r];
            
            while(l<size && currsum>rollsum) {
                currsum-=nums[l];
                l++;
            }
            if(currsum==rollsum) {
                maxlen = max(maxlen,r-l+1);
            }
        }
        
        if (maxlen == 0) return -1;
        return size-maxlen;
    }
};