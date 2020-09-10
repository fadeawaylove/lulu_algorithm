from typing import List
"""
递归
"""


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # 取出重复的单个字符串
        arr = [x for x in arr if len(x) == len(set(x))]

        return self.trace_back(0, "", arr)

    def trace_back(self, start, path, arr):
        # 结束条件
        if start >= len(arr):
            return len(path)
        else:
            # 如果当前最大字符串path与即将加入的字符串arr[start]不存在重复的
            # 则取添加和不添加中的较大值
            if not (set(path) & set(arr[start])):
                return max(self.trace_back(start + 1, path + arr[start], arr),
                           self.trace_back(start + 1, path, arr))
            # 存在重复则直接返回
            else:
                return self.trace_back(start + 1, path, arr)


print(Solution().maxLength(["jnfbyktlrqumowxd", "mvhgcpxnjzrdei"]))
# print(Solution().maxLength(["yy","bkhwmpbiisbldzknpm"]))
