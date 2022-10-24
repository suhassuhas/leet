class Solution {
public:
    unordered_set<char> charSet;
    bool overlap(unordered_set<char> cSet, string word) {
        unordered_set<char> prev;
        for(char c: word) {
            if(charSet.find(c) != charSet.end() or prev.find(c) != prev.end()) {
                return true;
            }
            prev.insert(c);
        }
        return false;
    }
    
    int backtrack(int i,vector<string>& arr) {
        if (i == arr.size()) {
            return charSet.size();
        }
        int res = 0;
        if (!overlap(charSet,arr[i])) {
            for(char c: arr[i]) {
                charSet.insert(c);
            }
            res = backtrack(i+1,arr);
            for(char c: arr[i]) {
                charSet.erase(c);
            }
        }
        return max(res,backtrack(i+1,arr));
    }
    
    int maxLength(vector<string>& arr) {
        return backtrack(0,arr);    
    }
};