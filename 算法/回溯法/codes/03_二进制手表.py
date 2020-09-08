"""
n中选k问题一般可以用回溯法，因为不知道k是多少
"""

from typing import List
from copy import copy


class Solution:
    # data = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
    data = [
        1,
        2,
        4,
        8,
        16,
        32,
        1,
        2,
        4,
        8,
    ]

    def readBinaryWatch(self, num: int) -> List[str]:
        if num == 0:
            return ["0:00"]

        visited = [False] * len(self.data)
        ret = []
        self.dfs(0, num, ret, [])
        return sorted(ret, key=lambda x: (int(x.split(":")[0]),int(x.split(":")[1])) )
        # return ret

    def dfs(self, start, num, ret, path):
        # 递归条件
        if len(path) == num:
            # 进行条件判断，看是否需要加入结果中
            hours = minutes = 0
            for i in path:
                if i > 5:
                    hours += self.data[i]
                else:
                    minutes += self.data[i]
            if hours <= 11 and minutes <= 59:
                temp = "%d:%0.2d" % (hours, minutes)
                # ret.append(temp)
            ret.append(path)
            return

        for i in range(start, len(self.data) - num + len(path) + 1):
            path.append(i)
            self.dfs(i + 1, num, ret, copy(path))
            path.pop()


print(Solution().readBinaryWatch(2))