// BF APPROACH
//  class Solution {
//  public:
//      int maxProduct(vector<int>& nums) {
//          int n = nums.size();
//          int ans=0;
//          vector<int>maxx;
//          for(int i=0;i<n;i+=1)
//          {
//              for(int j=i+1;j<n;j+=1)
//              {
//                  ans=(nums[i]-1)*(nums[j]-1);
//                  maxx.push_back(ans);
//              }
//          }
//          return *max_element(maxx.begin(),maxx.end());
//      }
//  };

// Priority queue soloution

// class Solution {
// public:
//     int maxProduct(vector<int>& nums) {
//         priority_queue<int>s;
//         for(int i=0;i<nums.size();i+=1)
//         {
//             s.push(nums[i]);
//         }
//         int storeone  = s.top();
//         s.pop();
//         int storetwo = s.top();
//         s.pop();
//         int ans = (storeone-1)*(storetwo-1);
//         return ans;
//     }
// };