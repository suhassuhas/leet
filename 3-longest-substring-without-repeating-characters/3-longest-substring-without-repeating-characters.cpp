class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char,int> seen;
        int n = s.size();
        int l = 0, output = 0;
        for(int r=0;r<n;r++) {
            if (seen.find(s[r])==seen.end()) {
                output = max(output,r-l+1);
            } else {
                auto pos = seen.find(s[r]);
                if (pos->second < l) {
                    output = max(output,r-l+1);
                } else {
                    l = pos->second + 1;
                }
            }
            seen[s[r]] = r;
        }
        return output;
    }
};

