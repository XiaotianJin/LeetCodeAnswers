from typing import List

class Solution1:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sum = 0
        visited = {}  # n->adder
        for num in nums:
            is_ok = False
            if num in visited:
                sum += visited[num]
                continue
            else:
                sqn = int(num**0.5)
                divisor = 0
                counter = 0
                for i in range(2, sqn+1):
                    if num % i == 0:
                        counter += 1
                        divisor += i
                    if counter > 1:
                        break
                if counter == 1:
                    other_divisor = num // divisor
                    if other_divisor != divisor:
                        data_to_add = (divisor + num + 1 + num/divisor)
                        sum += data_to_add
                        visited[num] = data_to_add
                        is_ok = True
                if not is_ok:
                    visited[num] = 0
        return int(sum)

class Solution:
    MAX = 10**5+1
    counter = [0]*MAX
    summer = [0]*MAX
    for i in range(1, MAX):
        for j in range(i, MAX, i):
            counter[j] += 1
            summer[j] += i
        
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if self.counter[num] == 4:
                res += self.summer[num]
        return res

if __name__ == '__main__':
    only_first_case = -1
    input_list = [
        ([21], 32),
        ([21,4,7], 32),
        ([21,21], 64),
        ([27], 1+3+9+27),
    ]
    failed_case = []
    if only_first_case < 0:
        for i, (digits, ans) in enumerate(input_list):
            res = Solution().sumFourDivisors(digits)
            print("Res = ", res, " Ans = ", ans, " pass = ", res == ans, " case = ", i)
            if res != ans:
                failed_case.append((i, digits, ans, res))
    else:
        digits, ans = input_list[only_first_case]
        res = Solution().sumFourDivisors(digits)
        print("Res = ", res, " Ans = ", ans, " pass = ", res == ans, " case = ", only_first_case)
        if res != ans:
            failed_case.append((only_first_case, digits, ans, res))
    
    if len(failed_case) == 0:
        print("!All case pass!")
    else:
        print("XXX Failed case:")
        for case in failed_case:
            print(case)