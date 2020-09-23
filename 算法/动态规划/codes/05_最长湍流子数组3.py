from typing import List
"""
如果 A[i-1] > A[i-2] and A[i] < A[i-1]
dp[i] = dp[i] + 1
"""


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        if n == 1:
            return 1

        op = []  # True代表大于 False代表小于 -1代表等于

        for i in range(1, n):
            op.append(self.get_op(A[i], A[i - 1]))
        print(op)

        m = 1
        for i in range(n - 1):
            cop = op[i]
            if i == 0:
                if op[0] == -1:
                    count = 1
                else:
                    count = 2
            else:
                pre_cop = op[i - 1]
                if cop == (not pre_cop):
                    count += 1
                else:
                    m = max(m, count)
                    if cop == -1:
                        count = 1
                    else:
                        count = 2
            if i == n - 2:
                m = max(m, count)

        return m

    def get_op(self, a, b):
        if a == b:
            return -1
        return a > b


print(Solution().maxTurbulenceSize([0, 8, 45, 88, 48, 68, 28, 55, 17, 24]))
print(Solution().maxTurbulenceSize(
    [250, 50, 219, 258, 199, 79, 36, 218, 218, 248]))
