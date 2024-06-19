class Solution {
public:
    bool checkdays(int mid, vector<int>& bloomDay, int m, int k) {
        int cc = 0, bq = 0;
        for (int i = 0; i < bloomDay.size(); i += 1) {
            if (bloomDay[i] <= mid) {
                // if the current is less than or equal to then add the cc
                cc += 1;
            } else {
                cc = 0;
            }
            if (cc == k) {
                // if we can able to make k bqs
                bq += 1;
                cc = 0;
            }
        }
        // return true if we can make posssible bqts
        return bq >= m;
    }
    int minDays(vector<int>& bloomDay, int m, int k) {
        int n = bloomDay.size();
        if ((long)m * k > n) {
            return -1;
        }
        int l = 0, r = *max_element(bloomDay.begin(), bloomDay.end());
        int ans = -1;
        while (l <= r) {
            int mid = (l + r) / 2;
            // check if mid no of days to make m bq to make k consecative
            // flowers
            if (checkdays(mid, bloomDay, m, k)) {
                ans = mid;
                // reduce for flowers
                r = mid - 1;
            } else {
                // increase
                l = mid + 1;
            }
        }
        return ans;
    }
};
