#include <vector>
#include <tuple>
#include <iostream>
#include <algorithm>
#include <functional>
#include <queue>

using namespace std;
typedef long long ll;

class Solution {
public:
    int mostBooked(int n, vector<vector<int>>& meetings) {

        std::sort(meetings.begin(), meetings.end(),
                  [](const vector<int>& a, const vector<int>& b)
                  {
                      return a[0] < b[0];
                  });
        std::priority_queue<ll, std::vector<ll>, std::greater<ll>> free;
        for (ll i = 0;i < n; i++)
        {
            free.push(i);
        }
        std::priority_queue<std::vector<ll>, std::vector<std::vector<ll>>, std::greater<std::vector<ll>>> busy;
        std::vector<int> counter(n, 0);

        ll max_room_id = -1;
        ll max_room_counter = -1;

        for (auto& meeting : meetings)
        {
            ll start = meeting[0], end = meeting[1];
            while (!busy.empty() && busy.top()[0] <= start)
            {
                free.push(busy.top()[1]);
                busy.pop();
            }

            ll end_time = -1;
            ll room_id = -1;
            if (!free.empty())
            {
                room_id = free.top();
                end_time = end;
                free.pop();
                // cout << "-> r = " << room_id << " e = " << end_time << '\n';
            }
            else if (!busy.empty())
            {
                room_id = busy.top()[1];
                end_time = busy.top()[0] + (end - start);
                busy.pop();
                // cout << "== r = " << room_id << " e = " << end_time << '\n';
            }
            busy.push({end_time, room_id});
            counter[room_id]++;
            if (counter[room_id] > max_room_counter)
            {
                max_room_counter = counter[room_id];
                max_room_id = room_id;
            }
            else if (counter[room_id] == max_room_counter && room_id < max_room_id)
            {
                max_room_id = room_id;
            }
        }

        return max_room_id;
    }
};

int main() {
    int only_this_case = -1;
    vector<tuple<int, vector<vector<int>>, int>> input_list = {
        {4, vector<vector<int>>{{48,49},{22,30},{13,31},{31,46},{37,46},{32,36},{25,36},{49,50},{24,34},{6,41}}, 0}, // Failed case 6
        {4, vector<vector<int>>{{12,44},{27,37},{48,49},{46,49},{24,44},{32,38},{21,49},{13,30}}, 1}, // Failed case 5
        {3, vector<vector<int>>{{1,27},{29,49},{47,49},{41,43},{15,36},{11,15}}, 1}, // Failed case 4
        {5, vector<vector<int>>{{12,18},{8,11},{19,20},{5,11}}, 0}, // Failed case 3
        {2, vector<vector<int>>{{10,11},{2,10},{1,17},{9,13},{18,20}}, 1}, // Failed case 2
        {4, vector<vector<int>>{{18,19},{3,12},{17,19},{2,13},{7,10}}, 0}, // Failed case 1
        {2, vector<vector<int>>{{0,10},{1,5},{2,7},{3,4}}, 0},
        {3, vector<vector<int>>{{1,20},{2,10},{3,5},{4,9},{6,8}}, 1},
    };

    vector<tuple<int, int, vector<vector<int>>, int, int>> failed_case;
    Solution sol;

    if (only_this_case == -1)
    {
        for (size_t i = 0; i < input_list.size(); ++i) {
            auto [n, meetings, ans] = input_list[i];
            int res = sol.mostBooked(n, meetings);
            cout << "Res = " << res << " Ans = " << ans
                << " pass = " << (res == ans ? "true" : "false")
                << " case = " << i << '\n';
            if (res != ans) {
                failed_case.emplace_back(i, n, meetings, ans, res);
            }
        }
    }
    else
    {
        auto [n, meetings, ans] = input_list[only_this_case];
        int res = sol.mostBooked(n, meetings);
        cout << "Res = " << res << " Ans = " << ans
            << " pass = " << (res == ans ? "true" : "false")
            << " case = " << only_this_case << '\n';
        if (res != ans) {
            failed_case.emplace_back(only_this_case, n, meetings, ans, res);
        }
    }



    if (failed_case.empty()) {
        cout << "!All case pass!\n";
    } else {
        cout << "XXX Failed case:\n";
        for (auto [idx, n, mt, ans, res] : failed_case) {
            cout << idx << " n= " << n << " ans=" << ans << " res=" << res << '\n';
        }
    }
    return 0;
}