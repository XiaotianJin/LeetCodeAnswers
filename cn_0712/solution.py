class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        total = sum(map(ord, s1)) + sum(map(ord, s2))

        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i, x in enumerate(s1):
            for j, y in enumerate(s2):
                if x == y:
                    f[i + 1][j + 1] = f[i][j] + ord(x)
                else:
                    f[i + 1][j + 1] = max(f[i][j + 1], f[i + 1][j])
        return total - f[n][m] * 2

if __name__ == '__main__':
    s1 = "sea"
    s2 = "eat"
    print(Solution().minimumDeleteSum(s1, s2))