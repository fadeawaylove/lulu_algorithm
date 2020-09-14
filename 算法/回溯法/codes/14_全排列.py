from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        res = []

        def trace_back(path):
            if len(path) == n:
                res.append(path)
                return

            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                trace_back(path + [nums[i]])
                used[i] = False

        trace_back([])
        return res
