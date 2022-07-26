"""
使用回溯:
回溯一般都要使用到递归，具体要注意的就是
1.当回溯的时候，状态要还原；
2.如何找到下一个搜索起点；
3.递归退出条件；
"""

from typing import List
from copy import copy


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        self.dfs(1, k, n, ret, [])
        return ret

    def dfs(self, start, k, n, ret, path):
        # 递归退出条件
        if len(path) == k:
            ret.append(path)
            return

        # for i in range(start, n + 1):
        for i in range(start, n - k + 1 + len(path) + 1):  #  优化
            # 加入path
            path.append(i)
            # 递归深度遍历
            self.dfs(i + 1, k, n, ret, copy(path))
            # 回溯还原状态
            path.pop()


print(Solution().combine(4, 2))
