from typing import List
"""
如果 A[i-1] > A[i-2] and A[i] < A[i-1]
dp[i] = dp[i] + 1
"""


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        dp = [None] * n
        op = [None] * n  # True代表大于 False代表小于 -1代表等于

        for i in range(n):
            if i == 0:
                dp[i] = 1
            if i == 1:
                op[i] = self.get_op(A[1], A[0])
                if op[i] == -1:
                    dp[i] = 1
                else:
                    dp[i] = 2
            if i > 1:
                cop = self.get_op(A[i], A[i - 1])
                op[i] = cop
                if cop == -1:
                    dp[i] = 1
                elif cop is not op[i - 1]:
                    dp[i] = dp[i - 1] + 1
                else:
                    dp[i] = 2
        print(dp)
        print(op)
        return max(dp)

    def get_op(self, a, b):
        if a == b:
            return -1
        return a > b


print(Solution().maxTurbulenceSize([0, 8, 45, 88, 48, 68, 28, 55, 17, 24]))
print(Solution().maxTurbulenceSize(
    [250, 50, 219, 258, 199, 79, 36, 218, 218, 248]))
