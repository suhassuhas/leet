class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string firstWord, secondWord;
        for (string word: word1) {
            firstWord += word;
        }
        for (string word:word2) {
            secondWord += word;
        }
        return firstWord == secondWord;
    }
};