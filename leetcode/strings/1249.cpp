class Solution
{
public:
    string minRemoveToMakeValid(string s)
    {
        int n = s.length();
        stack<int> stck;
        for (int i = 0; i < n; i += 1)
        {
            if (s[i] == '(')
            {
                stck.push(i);
            }
            else if (s[i] == ')')
            {
                if (stck.empty())
                {
                    s[i] = '*';
                }
                else
                {
                    stck.pop();
                }
            }
        }
        while (!stck.empty())
        {
            s[stck.top()] = '*';
            stck.pop();
        }
        s.erase(remove(s.begin(), s.end(), '*'), s.end());
        return s;
    }
};