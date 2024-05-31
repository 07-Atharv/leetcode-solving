class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        vector<int> ans;
        int n = nums.size();
        unordered_map<int, int> mp;

        for (int i = 0; i < n; i += 1) {
            mp[nums[i]] += 1;
        }

        for (auto& x : mp) {
            if (x.second == 1) {
                ans.push_back(x.first);
            }
        }

        return ans;
    }
};
