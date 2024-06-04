class Solution {
public:
    int longestPalindrome(string s) {
        int ans = 0, flag = 0;
        map<char, int> mp;
        for (auto& x : s) {
            mp[x] += 1;
        }
        for (auto& x : mp) {
            if (x.second > 1) {
                ans += x.second / 2 * 2;
            }
            if (x.second % 2 == 1) {
                // ans += (x.second - 1);
                flag = 1;
            }
        }
        return ans + flag;
    }
};
