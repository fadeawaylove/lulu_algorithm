"""
输入 0 -->[[]]
输入 1 -->[[],[1]]
输入 2 -->[[],[1],[2],[1,2]]
输入 3 -->[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
可以获得 递推公式： f(n) = f(n-1) + [i+[num] for i in f(n-1)]
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [
            [],
        ]
        if not nums:
            return res

        for num in nums:
            res += [arr + [num] for arr in res]
        return res


print(Solution().subsets([1, 2, 3]))
