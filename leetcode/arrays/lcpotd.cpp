class Solution
{
public:
    bool checkValidString(string s)
    {
        stack<int> openparen;
        stack<int> star;
        for (int i = 0; i < s.length(); i += 1)
        {
            if (s[i] == '(')
            {
                openparen.push(i);
            }
            else if (s[i] == '*')
            {
                star.push(i);
            }
            else
            {
                if (!openparen.empty())
                {
                    openparen.pop();
                }
                else if (!star.empty())
                {
                    star.pop();
                }
                else
                {
                    return 0;
                }
            }
        }
        while (!openparen.empty())
        {
            if (star.empty())
            {
                return 0;
            }
            else if (openparen.top() < star.top())
            {
                openparen.pop();
                star.pop();
            }
            else
            {
                return 0;
            }
        }
        return 1;
    }
};