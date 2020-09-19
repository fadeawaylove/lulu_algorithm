from typing import List
"""
如果 A[i-1] > A[i-2] and A[i] < A[i-1] 
dp[i] = dp[i] + 1 
"""


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        op = []  # True代表大于 False代表小于 -1代表等于

        for i in range(1, n):
            op.append(self.get_op(A[i], A[i-1]))
        print(op)

        m = 1
        count = 1
        for i in range(n-1):
            cop = op[i]
            if cop == (not op[i-1]):
                count += 1
            else:
                m = max(m, count)
                count = 1
                continue
            
        print(m)
        return m

    def get_op(self, a, b):
        if a == b:
            return -1
        return a > b


print(Solution().maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
print(Solution().maxTurbulenceSize(
    [250, 50, 219, 258, 199, 79, 36, 218, 218, 248]))
