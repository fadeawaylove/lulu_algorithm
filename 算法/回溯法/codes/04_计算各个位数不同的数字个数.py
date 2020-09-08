"""
其实就是10选n的问题
"""
from copy import copy


class Solution:
    def __init__(self):
        self.ret = 0
        self.data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def countNumbersWithUniqueDigits(self, n: int) -> int:

        self.dfs(n, [])
        return self.ret

    def dfs(self, n, path):
        if len(path) == n:
            print(path)
            self.ret += 1
            return

        choices = set(self.data) - set(path)
        # if path and (path[-1] != 0 or path == [0] * len(path)):
        #     choices.add(0)
        for i in choices:
            path.append(i)
            self.dfs(n, copy(path))
            path.pop()


print(Solution().countNumbersWithUniqueDigits(2))
