from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_count = 0
        min_abs = float('inf')
        sum = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                current = matrix[i][j]
                if current >= 0:
                    sum += matrix[i][j]
                else:
                    sum -= current
                    min_count += 1
                if min_abs > abs(current):
                    min_abs = abs(current)
        
        if min_count %2 == 1:
            sum -= 2*min_abs
        
        return sum

if __name__ == '__main__':
    only_first_case = -1
    input_list = [
        ([[1,-1],[-1,1]], 4),
        ([[1,2,3],[-1,-2,-3],[1,2,3]], 16),
    ]
    failed_case = []
    if only_first_case < 0:
        for i, (digits, ans) in enumerate(input_list):
            res = Solution().maxMatrixSum(digits)
            print("Res = ", res, " Ans = ", ans, " pass = ", res == ans, " case = ", i)
            if res != ans:
                failed_case.append((i, digits, ans, res))
    else:
        digits, ans = input_list[only_first_case]
        res = Solution().maxMatrixSum(digits)
        print("Res = ", res, " Ans = ", ans, " pass = ", res == ans, " case = ", only_first_case)
        if res != ans:
            failed_case.append((only_first_case, digits, ans, res))
    
    if len(failed_case) == 0:
        print("!All case pass!")
    else:
        print("XXX Failed case:")
        for case in failed_case:
            print(case)