from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def trace_back(start, path, total):
            if len(path) == total:
                res.append(path)
                return
            for i in range(start, n):
                trace_back(i + 1, path + [nums[i]], total)

        for x in range(n + 1):
            trace_back(0, [], x)
        return res
