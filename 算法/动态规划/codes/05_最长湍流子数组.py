from typing import List
"""
如果 A[i-1] > A[i-2] and A[i] < A[i-1]
dp[i] = dp[i] + 1
"""


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        dp = [None] * n

        for i in range(n):
            if i == 0:
                dp[i] = 1
            if i == 1:
                dp[i] = 1 if A[0] == A[1] else 2
            if i > 1:
                if (A[i] > A[i - 1]
                        and A[i - 1] < A[i - 2]) or (A[i] < A[i - 1]
                                                     and A[i - 1] > A[i - 2]):
                    dp[i] = dp[i - 1] + 1
                elif A[i] == A[i - 1]:
                    dp[i] = 1
                else:
                    dp[i] = 2
        print(dp)
        return max(dp)


print(Solution().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
print(Solution().maxTurbulenceSize(
    [250, 50, 219, 258, 199, 79, 36, 218, 218, 248]))
