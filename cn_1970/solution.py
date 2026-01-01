from collections import deque
from typing import List

class Solution1:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        start_connect_set = set()  # {[i,j]}
        new_connect_set = set()  # {[i,j]}
        day_count = 0
        grid = [[0] * col for _ in range(row)]
        
        def get_neighbors(i, j) -> bool:
            if grid[i][j] == 1:
                return False
            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni, nj = i+di, j+dj
                if 0<=ni<row and 0<=nj<col and grid[ni][nj] == 0 and (ni,nj) not in start_connect_set:
                    new_connect_set.add((ni,nj))
                    if ni == row-1:
                        return True
            return False
        
        for idx, cell in enumerate(cells):
            start_connect_set = set()
            grid[cell[0]-1][cell[1]-1] = 1
            for j in range(0, col):
                if grid[0][j] == 0:
                    start_connect_set.add((0,j))
            if len(start_connect_set) == 0:
                break  # 起点封死，不用考虑了
            
            is_today_ok = False
            new_connect_set = set()
            for i,j in start_connect_set:
                if get_neighbors(i,j):
                    is_today_ok = True
                    break
            while len(new_connect_set) > 0:
                start_connect_set.update(new_connect_set)
                last_connect_set = new_connect_set.copy()
                new_connect_set.clear()
                for i,j in last_connect_set:
                    if get_neighbors(i,j):
                        is_today_ok = True
                        break
                if is_today_ok:
                    break
            if not is_today_ok:
                return day_count
            day_count += 1
        return day_count

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left, right, ans = 0, row * col, 0
        while left <= right:
            mid = (left + right) // 2
            
            grid = [[1] * col for _ in range(row)]
            for x, y in cells[:mid]:
                grid[x - 1][y - 1] = 0

            q = deque()
            for i in range(col):
                if grid[0][i]:
                    q.append((0, i))
                    grid[0][i] = 0
            
            found = False
            while q:
                x, y = q.popleft()
                for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= nx < row and 0 <= ny < col and grid[nx][ny]:
                        if nx == row - 1:
                            found = True
                            break
                        q.append((nx, ny))
                        grid[nx][ny] = 0
            
            if found:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans

if __name__ == '__main__':
    only_first_case = 3
    input_list = [
        (2,2,[[1,1],[2,1],[1,2],[2,2]], 2),
        (2,2,[[1,1],[1,2],[2,1],[2,2]], 1),
        (3,3,[[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]],3),
        (13,9,[[12,6],[3,4],[2,9],[9,4],
               [9,2],[6,4],[4,4],[8,6],
               [4,9],[5,6],[7,5],[12,4],
               [11,8],[3,7],[2,6],[9,8],
               [3,5],[13,4],[1,3],[10,2],
               [8,9],[6,6],[11,7],[11,1],
               [13,9],[12,7],[10,7],[8,2],
               [1,8],[7,3],[6,5],[2,1],
               [10,6],[4,8],[4,2],[9,7],
               [6,2],[3,6],[12,2],[10,3],
               [10,5],[9,5],[8,8],[8,7],
               [3,2],[13,6],[3,1],[5,1],
               [2,7],[8,3],[12,5],[11,2],
               [6,3],[1,4],[13,3],[4,1],
               [9,9],[7,7],[4,3],[12,1],
               [2,2],[7,6],[4,6],[7,9],
               [7,2],[3,8],[1,6],[11,3],
               [11,4],[5,9],[13,8],[1,9],
               [10,1],[9,1],[6,1],[10,9],
               [12,9],[11,5],[8,1],[13,5],
               [9,6],[13,2],[6,8],[2,8],
               [5,3],[3,3],[13,1],[11,9],
               [9,3],[2,4],[5,2],[8,5],
               [13,7],[12,8],[5,5],[7,1],
               [7,4],[2,5],[6,9],[4,7],
               [5,8],[1,5],[10,8],[8,4],
               [1,1],[3,9],[1,2],[7,8],
               [1,7],[6,7],[11,6],[4,5],
               [5,7],[2,3],[10,4],[5,4],
               [12,3]],35)  # Failed case 1
    ]
    failed_case = []
    if only_first_case < 0:
        for i, (row,col,cells, ans) in enumerate(input_list):
            res = Solution().latestDayToCross(row, col, cells)
            print("Res = ", res, " Ans = ", ans, " pass = ", res == ans, " case = ", i)
            if res != ans:
                failed_case.append((i, row, col, cells, ans, res))
    else:
        row,col,cells, ans = input_list[only_first_case]
        res = Solution().latestDayToCross(row, col, cells)
        print("Res = ", res, " Ans = ", ans, " pass = ", res == ans, " case = ", only_first_case)
        if res != ans:
            failed_case.append((only_first_case, row, col, cells, ans, res))
    
    if len(failed_case) == 0:
        print("!All case pass!")
    else:
        print("XXX Failed case:")
        for case in failed_case:
            print(case)