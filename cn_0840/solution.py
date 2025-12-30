from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        possible_magic = [
            [4,3,8,9,5,1,2,7,6],
            [8,3,4,1,5,9,6,7,2],
            [4,9,2,3,5,7,8,1,6],
            [2,9,4,7,5,3,6,1,8],
            [8,1,6,3,5,7,4,9,2],
            [6,1,8,7,5,3,2,9,4],
            [6,7,2,1,5,9,8,3,4],
            [2,7,6,9,5,1,4,3,8]
        ]
        
        row = len(grid)
        col = len(grid[0])
        count = 0
                
        def is_magic(i, j) -> bool:
            if i < 1 or j < 1 or i > row-2 or j > col-2:
                return False
            for k in range(3):
                for l in range(3):
                    if grid[i-1+k][j-1+l] not in [1,2,3,4,5,6,7,8,9]:
                        return False
            for magic in possible_magic:
                # if grid[i-1][j-1:j+2] == magic[0] and grid[i-1+1][j-1:j+2] == magic[1] and grid[i-1+2][j-1:j+2] == magic[2]:
                #     return True
                # if grid[i-1:i+2][j-1][::-1] == magic[0] and grid[i-1:i+2][j-1+1][::-1] == magic[1] and grid[i-1:i+2][j-1+2][::-1] == magic[2]:
                #     return True
                new_grid = [grid[i-1+k][j-1+l] for k in range(3) for l in range(3)]
                if new_grid == magic:
                    return True
            return False
        
        for i in range(1, row-1):
            for j in range(1, col-1):
                if is_magic(i, j):
                    count += 1
        return count

if __name__ == '__main__':
    only_first_case = -1
    input_list = [
        ([[4,3,8,5,5,5],[9,5,1,5,5,5],[2,7,6,5,5,5]], -1),
    ]
    failed_case = []
    if only_first_case < 0:
        for i, (grid, ans) in enumerate(input_list):
            res = Solution().numMagicSquaresInside(grid)
            print("Res = ", res, " Ans = ", ans, " pass = ", res == ans, " case = ", i)
            if res != ans:
                failed_case.append((i, grid, res))
    else:
        grid, ans = input_list[only_first_case]
        res = Solution().numMagicSquaresInside(grid)
        print("Res = ", res, " Ans = ", ans, " pass = ", res == ans, " case = ", only_first_case)
        if res != ans:
            failed_case.append((only_first_case, grid, ans, res))
    
    if len(failed_case) == 0:
        print("!All case pass!")
    else:
        print("XXX Failed case:")
        for case in failed_case:
            print(case)