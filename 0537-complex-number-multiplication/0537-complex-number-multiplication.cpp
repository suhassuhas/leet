class Solution {
public:
    string complexNumberMultiply(string num1, string num2) {
        int fR = 0, fC = 0, sR = 0, sC = 0;
        sscanf(num1.c_str(), "%d+%di", &fR,&fC);
        sscanf(num2.c_str(), "%d+%di", &sR,&sC);
        return to_string(fR*sR-fC*sC)+"+"+to_string(fR*sC+fC*sR)+"i";
    }
};