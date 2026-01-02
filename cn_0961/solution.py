from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        shown_up = set()
        for i in nums:
            if i in shown_up:
                return i
            shown_up.add(i)