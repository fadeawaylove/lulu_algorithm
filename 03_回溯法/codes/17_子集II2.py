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
"""
使用迭代法
原数组[1,2,2]
[] -> []
[1] -> [] [1]
[1,2] -> [] [1]  - [2] [1,2]
[1,2,2] -> [] [1] [2] [1,2] {[2] [1,2]} [2,2] [1,2,2]
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        res = [[]]
        start = 0
        for i in range(n):
            temp = []
            for j in range(len(res)):
                if i > 0 and nums[i] == nums[i - 1] and j <= start:
                    continue
                temp.append(res[j] + [nums[i]])
            start = len(res) - 1
            res.extend(temp)
        return res


print(Solution().subsetsWithDup([4, 4, 4, 1, 4]))
# print(Solution().subsetsWithDup([1, 2, 2]))
