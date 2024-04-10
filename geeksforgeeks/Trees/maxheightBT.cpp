
#pragma GCC optimize("O3", "unroll-loops")
#pragma gcc optimize("Ofast")
#pragma GCC optimization("Ofast")
#pragma optimize(Ofast)

#include <bits/stdc++.h>
typedef long long ll;
typedef double d;
const int mod = 1000000007;
#define endl "\n";
#define all(a) a.begin(), a.end()
using namespace std;
struct Node
{
    int data;
    Node *left;
    Node *right;
    Node(int x)
    {
        data = x;
        left = right = NULL;
    }
};
int maxHeight(Node *root)
{
    if (root == NULL)
    {
        return;
    }
    int left = maxHeight(root->left);
    int right = maxHeight(root->right);
    return max(left, right) + 1;
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);
    auto start = std::chrono::high_resolution_clock::now();

    // Your Code

    auto end = std::chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::milliseconds>(end - start).count();
    cout << "Execution time: " << duration << " ms" << endl;
    return 0;
}
