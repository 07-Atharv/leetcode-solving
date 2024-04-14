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
    }
};
void spiralTraversal(Node *root)
{
    if (root == NULL)
    {
        return;
    }
    stack<int> stck;
    queue<Node *> q;
    bool rev = false;
    q.push(root);
    vector<int> ans;
    while (!q.empty())
    {
        int count = q.size();
        for (int i = 0; i < count; i += 1)
        {
            Node *curr = q.front();
            if (rev)
            {
                stck.push(curr->data);
            }
            else
            {
                ans.push_back(curr->data);
            }
            if (curr->left)
            {
                q.push(curr->left);
            }
            if (curr->right)
            {
                q.push(curr->right);
            }
        }
        if (rev)
        {
            while (!stck.empty())
            {
                ans.push_back(stck.top());
                stck.pop();
            }
        }
        rev = !rev;
    }
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