from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0
    
        n = len(grid)
        m = len(grid[0])
        last_pos_idx = m - 1
        pos_sum = 0
        
        for row in grid:
            current_pos_idx = last_pos_idx
            while current_pos_idx >= 0 and row[current_pos_idx] < 0:
                current_pos_idx -= 1
            pos_sum += current_pos_idx + 1
            last_pos_idx = current_pos_idx
        
        return n*m - pos_sum
    

if __name__ == '__main__':
    only_first_case = -1
    input_list = [
        ([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]], 8)
    ]
    failed_case = []
    if only_first_case < 0:
        for i, (grid, ans) in enumerate(input_list):
            res = Solution().countNegatives(grid)
            print("Res = ", res, " Ans = ", ans, " pass = ", res == ans, " case = ", i)
            if res != ans:
                failed_case.append((i, grid, ans, res))
    else:
        grid, ans = input_list[only_first_case]
        res = Solution().countNegatives(grid)
        print("Res = ", res, " Ans = ", ans, " pass = ", res == ans, " case = ", only_first_case)
        if res != ans:
            failed_case.append((only_first_case, grid, ans, res))
    
    if len(failed_case) == 0:
        print("!All case pass!")
    else:
        print("XXX Failed case:")
        for case in failed_case:
            print(case)