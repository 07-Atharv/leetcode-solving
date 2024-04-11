class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        int n = deck.size();
        sort(deck.begin(), deck.end());
        queue<int> temp;

        for (int i = 0; i < n; i += 1) {
            temp.push(i);
        }
        vector<int> ans(n);
        for (int i = 0; i < n; i += 1) {
            ans[temp.front()] = deck[i];
            temp.pop();
            if (!temp.empty()) {
                temp.push(temp.front());
                temp.pop();
            }
        }
        return ans;
    }
};