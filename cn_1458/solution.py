from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        visited = {}
        def f(i, j):
            if i < 0 or j < 0:
                return float("-inf")
            if (i, j) in visited:
                return visited[(i, j)]
            no_i = f(i-1, j)
            no_j = f(i, j-1)
            no_ij = f(i-1, j-1)
            only_ij = nums1[i]*nums2[j]
            both_ij = only_ij + no_ij if no_ij > 0 else only_ij
            res = max(no_i, no_j, both_ij, no_ij, only_ij)
            visited[(i, j)] = res
            return res
        
        return f(len(nums1)-1, len(nums2)-1)

if __name__ == '__main__':
    only_first_case = -1
    input_list = [
        ([13,-7,12,-15,-7,8,3,-7,-5,13,-15,-8,5,7,-1,3,-11,-12,2,-12], [-1,13,-4,-2,-13,2,-4,6,-9,13,-8,-3,-9], 18),
        ([2,1,-2,5], [3,0,-6], 18),
        ([3,-2], [2,-6,7], 21),
        ([-1,-1], [1,1], -1),
    ]
    failed_case = []
    if only_first_case < 0:
        for i, (num1, num2, ans) in enumerate(input_list):
            res = Solution().maxDotProduct(num1, num2)
            print("Res = ", res, " Ans = ", ans, " pass = ", res == ans, " case = ", i)
            if res != ans:
                failed_case.append((i, num1, num2, ans))
    else:
        num1, num2, ans = input_list[only_first_case]
        res = Solution().maxDotProduct(num1, num2)
        print("Res = ", res, " Ans = ", ans, " pass = ", res == ans, " case = ", only_first_case)
        if res != ans:
            failed_case.append((only_first_case, num1, num2, ans, res))
    
    if len(failed_case) == 0:
        print("!All case pass!")
    else:
        print("XXX Failed case:")
        for case in failed_case:
            print(case)