from copy import copy
from typing import List

"""
动态规划优化
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 使用dp将所有回文存储起来dp[i][j]表示s[i:j+1]是否是回文字符串
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for right in range(n):
            for left in range(right + 1):
                # 左右边界字符相等，并且去掉左右边界的子字符串是回文
                if s[left] == s[right] and (right - left <= 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True

        ret = []
        self.dfs(0, s, [], ret, dp)
        return ret

    def dfs(self, start, s, path, ret, dp):
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
            if not dp[start][i]:
                continue
            path.append(s[start: i + 1])
            self.dfs(i + 1, s, copy(path), ret, dp)
            path.pop()


print(Solution().partition("aab"))
