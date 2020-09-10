
<!-- TOC -->

- [回溯法](#回溯法)
    - [1.单词搜索](#1单词搜索)
    - [2.组合](#2组合)
    - [3.二进制手表](#3二进制手表)
    - [4.分割回文串](#4分割回文串)
        - [方法1：回溯](#方法1回溯)
        - [方法2：DP优化](#方法2dp优化)
    - [5.字母组合迭代器](#5字母组合迭代器)
    - [5.开心字符串](#5开心字符串)
        - [解法1：回溯](#解法1回溯)
        - [解法2：数学方法](#解法2数学方法)

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

## 4.分割回文串
直通车：[https://leetcode-cn.com/problems/palindrome-partitioning/](https://leetcode-cn.com/problems/palindrome-partitioning/)

### 方法1：回溯

> 分析：问题第一眼看上去就像是n中选择k的问题，不同的是此题中的k可能是变化的，也就是说在一次选择的过程中，这个k可能都不同，画出递归树如下：

![https://raw.githubusercontent.com/fadeawaylove/article-images/master/%E5%88%86%E5%89%B2%E5%9B%9E%E6%96%87%E4%B8%B2.jpg](https://raw.githubusercontent.com/fadeawaylove/article-images/master/%E5%88%86%E5%89%B2%E5%9B%9E%E6%96%87%E4%B8%B2.jpg)

步骤：  
1. 从1到n（字符串s的长度）开始截取字符串，判断截取出的字符串是否是回文字符串：
    - 是回文：执行第2步
    - 不是回文：直接结束
2. 对截取后剩下的字符串进行步骤1的操作

```python3
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

```

### 方法2：DP优化
> 时间换空间，将字符串s中的回文子串的状态提前算出来，DP的状态转移方程就是:DP[i][j]为回文，则DP[i-1][j+1]为回文并且s[i]=s[j]（注意临界情况，j-i<=2即子串不可再分）

```python3
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

```

## 5.字母组合迭代器
直通车：[https://leetcode-cn.com/problems/iterator-for-combination/](https://leetcode-cn.com/problems/iterator-for-combination/)

```python3
class CombinationIterator:
    """
        其实就是一个n中选k，使用回溯法
    """
    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        ret = []
        self.dfs(0, [], ret, len(characters), combinationLength)
        self.ret = ret
        self.cur = -1

    def dfs(self, start, path, ret, n, k):
        if len(path) == k:
            ret.append("".join(path))
            return

        for i in range(start, n):
            path.append(self.characters[i])
            self.dfs(i + 1, path[:], ret, n, k)
            path.pop()

    def next(self) -> str:
        if self.hasNext():
            self.cur += 1
            return self.ret[self.cur]


    def hasNext(self) -> bool:
        if self.cur + 1 >= len(self.ret):
            return False
        return True


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
obj = CombinationIterator("abc", 2)

print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
```

## 5.开心字符串
直通车：[https://leetcode-cn.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/](https://leetcode-cn.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)

### 解法1：回溯

```python3
class Solution:
    data = ['a', 'b', 'c']

    def getHappyString(self, n: int, k: int) -> str:
        res = []
        self.dfs(0,n,[],res, k)
        if k > len(res):
            return ""
        return "".join(res[k-1])


    def dfs(self, start, n, path, res, k):
        if len(path) == n:
            res.append(path)
            return
        
        for i in self.data:
            # 剪枝
            if path and path[-1] == i:
                continue
            path.append(i)
            self.dfs(0, n, path[:], res, k)
            # 优化，当结果满足k个后，直接返回
            if len(res) >= k:
                return
            path.pop()
```

### 解法2：数学方法
![https://raw.githubusercontent.com/fadeawaylove/article-images/master/%E5%BC%80%E5%BF%83%E5%AD%97%E7%AC%A6%E4%B8%B2.jpg](https://raw.githubusercontent.com/fadeawaylove/article-images/master/%E5%BC%80%E5%BF%83%E5%AD%97%E7%AC%A6%E4%B8%B2.jpg)

> 思路：如上图所示，问题可以转化为求上述满树的第k个元素,这个树满足每个左节点都小于右结点，每个结点的值只能在a,b,c中选取。根据图示的数学特性，当层数等于n的时候，(k-1)//2^(n-1)可以确定属于那一颗子树，重复这个操作就可以找到最终的叶子节点。

```python3
class Solution:
    data = ['a', 'b', 'c']

    def getHappyString(self, n: int, k: int) -> str:
        # 长度超出直接返回
        if k > 3 * 2**(n - 1):
            return ""
        base = {"":["a", "b", "c"], "a": ["b", "c"], "b":["a", "c"], "c":["a", "b"]}

        res = ""
        k -= 1
        for i in range(n, 0, -1):
            x, k = k // 2**(i-1), k % 2**(i-1)
            if res:
                res += base[res[-1]][x]
            else:
                res = base[res][x]
        return res


print(Solution().getHappyString(3, 9))
```