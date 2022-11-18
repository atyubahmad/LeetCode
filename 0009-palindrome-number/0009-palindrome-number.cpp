class Solution {
public:
    bool isPalindrome(int x) {
        string strX = to_string(x);
        string revX = to_string(x);
        reverse(revX.begin(), revX.end());
        if(strX == revX)
            return true;
        return false;
    }
};