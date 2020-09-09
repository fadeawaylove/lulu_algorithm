"""
需要使用回溯法
"""

from copy import copy
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        self.dfs(0, s, [], ret)
        return ret

    def dfs(self, start, s, path, ret):
        """

        :param start: 开始截取的位置
        :param s:  原始字符串
        :param path: 记录截取路径，保存s的子串
        :param ret:  最终结果
        :return:
        """
        # 递归终止条件，截取下标等于字符串长度了，说明最终截取就是空了
        if start == len(s):
            ret.append(path)
            return

        # start是开始截取的下标
        for i in range(start, len(s)):
            # 不是回文字符串，剪枝
            if not self.check(s, start, i):
                continue
            path.append(s[start:i + 1])
            self.dfs(i + 1, s, copy(path), ret)
            path.pop()

    @staticmethod
    def check(s, start, end):
        """
        判断是不是回文字符串
        :param s: 主字符串
        :param start: 子串开始下标
        :param end: 子串结束下标
        :return:
        """
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


print(Solution().partition("aab"))
