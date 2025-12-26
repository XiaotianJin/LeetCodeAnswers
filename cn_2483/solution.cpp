#include <vector>
#include <string>
#include <iostream>

using namespace std;
class Solution1 {
public:
    int bestClosingTime(string customers) {
        vector<int> postive(customers.size() + 1, 0);
        vector<int> negative(customers.size() + 1, 0);
        int postive_count = 0;
        for (int i = 0; i < customers.size(); i++)
        {
            int hour = i+1;
            char this_char = customers[i];
            if (this_char == 'N')
            {
                postive_count += 1;
            }
            postive[hour] = postive_count;
        }
        int negative_count = 0;
        for (int i = customers.size()-1; i >= 0; i--)
        {
            int hour = i+1;
            char this_char = customers[i];
            if (this_char == 'Y')
            {
                negative_count += 1;
            }
            negative[i] = negative_count;
        }
        int ans = 0;
        int current_min = 1e9;
        for (int i = 0; i < postive.size(); i++)
        {
            int this_ans = postive[i] + negative[i];
            if (this_ans < current_min)
            {
                current_min = this_ans;
                ans = i;
            }
        }
        return ans;
    }
};

class Solution {
public:
    int bestClosingTime(string customers) {
        int cost = 0;
        int min_cost = 0;
        int hour = 0;
        for (int i = 0; i < customers.size(); i++)
        {
            if (customers[i] == 'N')
            {
                cost += 1;
            }
            else
            {
                cost -= 1;
            }
            if (cost < min_cost)
            {
                min_cost = cost;
                hour = i+1;
            }
        }
        return hour;
    }
};

int main()
{
    Solution s;
    string customers = "YYNY";
    cout << s.bestClosingTime(customers) << endl;
    // cout << "helloword" << endl;
    return 0;
}