#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;

class Solution {
public:
    int countNegatives(vector<vector<int>>& grid)
    {
        if (grid.size() == 0)
        {
            return 0;
        }
        int n = grid.size();
        int m = grid[0].size();
        int pos_sum = 0;
        int last_pos = m - 1;
        for (int i = 0; i < n; i++)
        {
            for (int j = last_pos; j >= 0; j--)
            {
                if (grid[i][j] >= 0)
                {
                    last_pos = j;
                    pos_sum += j + 1;
                    break;
                }
            }
        }

        return n*m - pos_sum;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int only_first_case = -1;
    vector<pair<vector<vector<int>>, int>> input_list = {
        {{{4,3,2,-1},{3,2,1,-1},{1,1,-1,-2},{-1,-1,-2,-3}}, 8}
    };

    vector<tuple<int, vector<vector<int>>, int, int>> failed_case;
    Solution sol;

    if (only_first_case < 0) {
        for (size_t i = 0; i < input_list.size(); ++i) {
            auto [grid, ans] = input_list[i];
            int res = sol.countNegatives(grid);
            cout << "Res = " << res << " Ans = " << ans
                 << " pass = " << (res == ans ? "true" : "false")
                 << " case = " << i << '\n';
            if (res != ans) {
                failed_case.emplace_back(i, grid, ans, res);
            }
        }
    } else {
        auto [grid, ans] = input_list[only_first_case];
        int res = sol.countNegatives(grid);
        cout << "Res = " << res << " Ans = " << ans
             << " pass = " << (res == ans ? "true" : "false")
             << " case = " << only_first_case << '\n';
        if (res != ans) {
            failed_case.emplace_back(only_first_case, grid, ans, res);
        }
    }

    if (failed_case.empty()) {
        cout << "!All case pass!\n";
    } else {
        cout << "XXX Failed case:\n";
        for (auto [idx, g, a, r] : failed_case) {
            cout << idx << ' ' << a << ' ' << r << '\n';
        }
    }
    return 0;
}