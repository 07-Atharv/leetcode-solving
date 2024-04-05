// class Solution {
// public:
//     string truncateSentence(string s, int k) {
//         string ans="";
//         int n = s.size();
//         for(int i=0;i<n;i++)
//         {
//             if(isblank(s[i]))
//             {
//                 k-=1;
//             }
//             if(k>0)
//             {
//                 ans+=s[i];
//             }
//         }
//         return ans;
//     }
// };