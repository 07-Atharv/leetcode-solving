//{ Driver Code Starts
// Initial Template for C++
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++
class Solution
{
public:
    int nthFibonacci(int n)
    {
        long long mod = 1e9 + 7;
        if (n <= 1)
        {
            return n;
        }
        int arr[n];
        arr[0] = 0;
        arr[1] = 1;
        for (int i = 2; i <= n; i += 1)
        {
            arr[i] = (arr[i - 1] + arr[i - 2]) % mod;
        }
        return arr[n];
    }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        Solution ob;
        cout << ob.nthFibonacci(n) << endl;
    }
    return 0;
}

// } Driver Code Ends