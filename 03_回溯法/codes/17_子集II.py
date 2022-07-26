"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        res = []

        def trace_back(start, path, total):
            if len(path) == total:
                res.append(path)
                return
            for i in range(start, n):
                # 只需判断是否和上一个数字相同
                if nums[i] == nums[i-1] and i > start:
                    continue
                trace_back(i + 1, path + [nums[i]], total)

        for x in range(n + 1):
            trace_back(0, [], x)
        return res


print(Solution().subsetsWithDup([4, 4, 4, 1, 4]))
