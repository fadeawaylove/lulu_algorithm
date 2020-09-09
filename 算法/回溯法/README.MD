
<!-- TOC -->

- [回溯法](#回溯法)
    - [1.单词搜索](#1单词搜索)
    - [2.组合](#2组合)
    - [3.二进制手表](#3二进制手表)

<!-- /TOC -->


# 回溯法
> 回溯法（探索与回溯法）是一种选优搜索法，又称为试探法，按选优条件向前搜索，以达到目标。但当探索到某一步时，发现原先选择并不优或达不到目标，就退回一步重新选择，这种走不通就退回再走的技术为回溯法，而满足回溯条件的某个状态的点称为“回溯点”。

## 1.单词搜索
直通车：[https://leetcode-cn.com/problems/word-search/](https://leetcode-cn.com/problems/word-search/)

> 分析：    
1. 首先规定一个搜索起点，这个起点就是字母矩阵中的任意一个点
2. 采用DFS（深度优先遍历）,每次判断有两种情况：当前值等于word对应值时，对当前下标做上判断过的标记，然后移动到下一个点继续当前的逻辑，如果相邻的点都满足，那么将当前标记的点取消；当前值与word对应的值不相等时，返回False。

```python3
from typing import List


class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)  # 行数
        if m == 0:
            return False
        n = len(board[0])  # 列数

        marked = [[False] * n for _ in range(m)]  # 记录每个位置被访问的状态

        # 从第一个开始检查是否有符合的
        for i in range(m):
            for j in range(n):
                if self._check(board, i, j, marked, 0, word, m, n):
                    return True
        return False

    def _check(self, board, start_x, start_y, marked, index, word, m, n):
        # 递归终止条件
        if index == len(word) - 1:
            return board[start_x][start_y] == word[index]

        # 中间匹配了继续搜索
        if board[start_x][start_y] == word[index]:
            # 匹配成功则标记下
            marked[start_x][start_y] = True
            # 寻找下一个位置
            for direction in self.directions:
                new_x = start_x + direction[0]
                new_y = start_y + direction[1]
                if 0 <= new_x < m and 0 <= new_y < n \
                        and not marked[new_x][new_y] and \
                        self._check(board, new_x, new_y, marked, index + 1, word, m, n):
                    return True
            marked[start_x][start_y] = False
        return False
```

## 2.组合
直通车：[https://leetcode-cn.com/problems/combinations/](https://leetcode-cn.com/problems/combinations/)

```python3
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

        # start初始是1
        for i in range(start, n + 1):
            # 加入path
            path.append(i)
            # 递归深度遍历
            self.dfs(i + 1, k, n, ret, copy(path))
            # 回溯还原状态
            path.pop()


print(Solution().combine(4, 2))
```

## 3.二进制手表
直通车：[https://leetcode-cn.com/problems/binary-watch/](https://leetcode-cn.com/problems/binary-watch/)

> 分析：还是使用回溯法，一般集合中选取若干的问题都可以转化为回溯法，需要注意以下几点：
1. 递归跳出的条件；
2. 记录历史状态，此例使用path，当回溯的时候需要将状态还原，此例中使用path.pop()还原；
3. 循环选取下一步时候的范围，一般可以优化；

```python3
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
```



