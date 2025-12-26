class Solution1:
    def bestClosingTime(self, customers: str) -> int:
        postive = [0]*(len(customers)+1)
        negative = [0]*(len(customers)+1)
        postive_count = 0
        for i, c in enumerate(customers):
            hour = i + 1
            idx = i
            this_char = c
            if this_char == 'N':
                postive_count += 1
            postive[hour] = postive_count
        negative_count = 0
        for i, c in enumerate(customers[::-1]):
            hour = len(customers) - i
            idx = len(customers) - i - 1
            this_char = c
            if this_char == 'Y':
                negative_count += 1
            negative[hour] = negative_count
        negative[0] = negative[1] + 1  # 因为题目给出了1 <= customers.length <= 10^5的条件，这里不用考虑判断 negative index的问题
        ans = float('inf')
        current_min = float('inf')
        for i in range(0, len(customers)+1):
            this_ans = postive[i] + negative[i]
            if this_ans < current_min:
                current_min = this_ans
                ans = i
        # print(f"input: {customers}\npos: {postive}\nneg: {negative}\nans: {ans}\n----------")
        return ans

class Solution2:
    def bestClosingTime(self, customers: str) -> int:
        postive = [0]*(len(customers)+1)
        negative = [0]*(len(customers)+1)
        ans = float('inf')
        current_min = float('inf')
        postive_count = 0
        for i, c in enumerate(customers):
            hour = i + 1
            this_char = c
            if this_char == 'N':
                postive_count += 1
            postive[hour] = postive_count
        negative_count = 0
        for i, c in enumerate(customers[::-1]):
            hour = len(customers) - i
            this_char = c
            if this_char == 'Y':
                negative_count += 1
            negative[hour] = negative_count
            this_ans = postive[hour] + negative[hour]
            if this_ans <= current_min:
                current_min = this_ans
                ans = hour
        negative[0] = negative[1] + 1  # 因为题目给出了1 <= customers.length <= 10^5的条件，这里不用考虑判断 negative index的问题
        this_ans = postive[0] + negative[0]
        if this_ans <= current_min:
            current_min = this_ans
            ans = 0
        # print(f"input: {customers}\npos: {postive}\nneg: {negative}\nans: {ans}\n----------")
        return ans

class Solution:
    # 有没有O(N)的办法呢，没想到，来抄一下答案：
    def bestClosingTime(self, customers: str) -> int:
        min_penalty = penalty = ans = 0
        for i,c in enumerate(customers):
            if c == "N":
                penalty += 1
            else:
                penalty -= 1

            if penalty < min_penalty:
                min_penalty = penalty
                ans = i+1
        return ans


if __name__ == '__main__':
    customers_and_res = [
        ("YYNY", 2),
        ("NNNNN", 0),
        ("YYYYY", 5),
        ("YN", 1),
        ("YNYNNNYYY", 9)
    ]
    failed_case = []
    for customers, ans in customers_and_res:
        res = Solution().bestClosingTime(customers)
        print("Res = ", res, " Ans = ", ans, " pass = ", res == ans)
        if res != ans:
            failed_case.append((customers, ans, res))
    
    if len(failed_case) == 0:
        print("!All case pass!")
    else:
        print("XXX Failed case:")
        for case in failed_case:
            print(case)