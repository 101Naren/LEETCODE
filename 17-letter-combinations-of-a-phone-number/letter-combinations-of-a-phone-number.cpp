class Solution {
public:

    void comb(vector<string>&ans, map<char, string>&m, string digits, int k, string curr){
        if(k == digits.size()){
            ans.push_back(curr);
        }
        for(char c: m[digits[k]]){
            comb(ans, m, digits, k+1, curr+c);
        }
    }

    vector<string> letterCombinations(string digits) {
        map<char, string>m;
        m['2'] = "abc";
        m['3'] = "def";
        m['4'] = "ghi";
        m['5'] = "jkl";
        m['6'] = "mno";
        m['7'] = "pqrs";
        m['8'] = "tuv";
        m['9'] = "wxyz";

        vector<string>ans;
        string curr = "";
        comb(ans, m, digits, 0, curr);

        return ans;
        

    }
};