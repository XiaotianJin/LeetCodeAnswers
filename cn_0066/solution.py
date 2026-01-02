from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits

if __name__ == '__main__':
    only_first_case = -1
    input_list = [
        ([1,2,3], [1,2,4]),
        ([9], [1,0]),
        ([9,9,9], [1,0,0,0]),
        ([9,9,8], [9,9,9]),
    ]
    failed_case = []
    if only_first_case < 0:
        for i, (digits, ans) in enumerate(input_list):
            res = Solution().plusOne(digits)
            print("Res = ", res, " Ans = ", ans, " pass = ", res == ans, " case = ", i)
            if res != ans:
                failed_case.append((i, digits, ans, res))
    else:
        digits, ans = input_list[only_first_case]
        res = Solution().plusOne(digits)
        print("Res = ", res, " Ans = ", ans, " pass = ", res == ans, " case = ", only_first_case)
        if res != ans:
            failed_case.append((only_first_case, digits, ans, res))
    
    if len(failed_case) == 0:
        print("!All case pass!")
    else:
        print("XXX Failed case:")
        for case in failed_case:
            print(case)