class Solution:
    def numOfWays(self, n: int) -> int:
        MOD=10**9+7
        aba = 6
        abc = 6
        n = n-1
        while(n > 0):
            new_aba = aba * 3 + abc * 2
            new_abc = aba * 2 + abc * 2
            aba = new_aba
            abc = new_abc
            n=n-1
        return (aba + abc) % MOD
        