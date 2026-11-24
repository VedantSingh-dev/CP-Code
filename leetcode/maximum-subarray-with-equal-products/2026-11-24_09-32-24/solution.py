import math
from typing import List


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        ans = 0
        p = [nums[0]]
        for i in range(1, n):
            p.append(nums[i] * p[i - 1])

        for i in range(n):
            for j in range(i, n):
                a = math.gcd(*nums[i : j + 1]) * math.lcm(*nums[i : j + 1])
                prod = p[j] if i == 0 else p[j] // p[i - 1]

                if a == prod:
                    ans = max(ans, j - i + 1)

        return ans