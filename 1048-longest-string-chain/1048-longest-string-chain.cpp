class Solution {
public:
    static bool f(string &l,string &r) {
        return l.size() < r.size();
    }
    
    int longestStrChain(vector<string>& words) {
        sort(words.begin(),words.end(),f);
        unordered_map<string,int> dp;
        int result = 1;
        string prev;
        for(string w:words) {
            dp[w] = 1;
            for(int i=0;i<w.size();i++) {
                prev = w.substr(0,i) + w.substr(i+1);
                if(dp.find(prev)!=dp.end()) {
                    dp[w] = max(dp[w],1+dp[prev]);
                    result = max(dp[w],result);           
                }
            }
        }
        return result;
    }
};