class Solution {
public:
    int lcs(string word1,string word2,int s1, int s2) {
        int dp[s1+1][s2+2];
        for(int i=0;i<=s1;i++) {
            for(int j=0;j<=s2;j++) {
                dp[i][j]=0;
            }
        }
        for(int i=0;i<=s1;i++) {
            for(int j=0;j<=s2;j++){
                if(i==0 || j==0) {
                    continue;
                }   
                if(word1[i-1]==word2[j-1]){
                    dp[i][j] = 1+dp[i-1][j-1];
                } else {
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
                }
            }            
        }
        return dp[s1][s2];
    }
    
    int minDistance(string word1, string word2) {
        int s1 = word1.length();
        int s2 = word2.length();
        int m  = lcs(word1,word2,s1,s2);
        return s1+s2-(2*m);
    }
};