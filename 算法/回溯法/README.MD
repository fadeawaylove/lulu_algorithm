
<!-- TOC -->

- [回溯法](#回溯法)
    - [1.单词搜索](#1单词搜索)
    - [2.组合](#2组合)
    - [3.二进制手表](#3二进制手表)
    - [4.分割回文串](#4分割回文串)
        - [方法1：回溯](#方法1回溯)
        - [方法2：DP优化](#方法2dp优化)
    - [5.字母组合迭代器](#5字母组合迭代器)
    - [6.开心字符串](#6开心字符串)
        - [解法1：回溯](#解法1回溯)
        - [解法2：数学方法](#解法2数学方法)
    - [7.将数组拆分为斐波那契序列](#7将数组拆分为斐波那契序列)
        - [方法1：回溯法](#方法1回溯法)
        - [方法2：暴力法](#方法2暴力法)
    - [8.08_组合总和 III](#808_组合总和-iii)
    - [9.串联字符串的最大长度](#9串联字符串的最大长度)
        - [方法1：回溯](#方法1回溯-1)
        - [方法2：递归](#方法2递归)
    - [10.组合总数](#10组合总数)
    - [11.有重复字符串的排列组合](#11有重复字符串的排列组合)
    - [12.无重复字符串的排列组合](#12无重复字符串的排列组合)
    - [13.字符串的排列](#13字符串的排列)
    - [14.全排列](#14全排列)
        - [方法一：回溯（辅助used列表）](#方法一回溯辅助used列表)
        - [方法二：回溯（交换法）](#方法二回溯交换法)
    - [15.幂集](#15幂集)
        - [方法1：回溯](#方法1回溯-2)
        - [方法2：递推](#方法2递推)
    - [16.电话号码的字母组合](#16电话号码的字母组合)
    - [17.子集Ⅱ](#17子集ⅱ)
        - [方法1：回溯法](#方法1回溯法-1)
        - [方法2：递推法](#方法2递推法)

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

## 6.开心字符串
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

## 7.将数组拆分为斐波那契序列
直通车：[https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence/](https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence/)

### 方法1：回溯法

```python3
from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        ret = []
        self.dfs(0, len(S), [], S, ret)
        if ret:
            return [int(x) for x in ret[0]]
        return ret

    def dfs(self, start, n, path, s, ret):
        if start == n and len(path) > 2:
            ret.append(path)
            return

        for i in range(start, n):
            temp = s[start:i + 1]
            # 跳过
            if len(path) >= 2:
                if not self.check(path[-2], path[-1], temp):
                    continue
            # 剪枝
            if (temp.startswith("0") and temp != "0") or int(temp) > 2 ** 31 - 1:
                return
            self.dfs(i + 1, n, path[:] + [temp], s, ret)

    def check(self, astr, bstr, cstr):
        if int(astr) + int(bstr) == int(cstr):
            return True
        return False


print(Solution().splitIntoFibonacci("123456579"))
print(Solution().splitIntoFibonacci("1101111"))
print(Solution().splitIntoFibonacci("0123"))
print(Solution().splitIntoFibonacci(
    "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"))

```

### 方法2：暴力法
待补充。。。


## 8.08_组合总和 III
直通车：[https://leetcode-cn.com/problems/combination-sum-iii/](https://leetcode-cn.com/problems/combination-sum-iii/)

依然回溯+剪枝

```python3

from typing import List


class Solution:
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.back_trace(0, 9, res, [], k, n)
        return res

    def back_trace(self, start, total, res, path, k, n):
        # 递归跳出条件
        if len(path) == k:
            res.append(path)
            return

        for i in range(start, total):
            # 跳过
            if len(path) == k - 1:
                if sum(path) + self.data[i] != n:
                    continue
            self.back_trace(i + 1, total, res, path + [self.data[i]], k, n)


print(Solution().combinationSum3(3, 7))
print(Solution().combinationSum3(3, 9))

```

## 9.串联字符串的最大长度
直通车：[https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/](https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/)
### 方法1：回溯
```python3
from typing import List


class Solution:
    def __init__(self):
        self.res = 0

    def maxLength(self, arr: List[str]) -> int:

        for i in range(1, len(arr) + 1):
            self.trace_back(0, [], arr, i)
        return self.res

    def trace_back(self, start, path, arr, k):
        # 结束条件
        if len(path) == k:
            self.res = max(self.res, len("".join(path)))
            return

        for i in range(start, len(arr)):
            if not self.check_single(arr[i]):
                continue
            if len(path) >= 1:
                if not self.check_multiple(path, arr[i]):
                    continue
            self.trace_back(i + 1, path + [arr[i]], arr, k)

    def check_multiple(self, origin_str, target_str):
        origin_str = "".join(origin_str)
        return self.check_single(origin_str + target_str)

    def check_single(self, a_str):
        return len(set(a_str)) == len(a_str)


# print(Solution().maxLength(["jnfbyktlrqumowxd", "mvhgcpxnjzrdei"]))
print(Solution().maxLength(["yy","bkhwmpbiisbldzknpm"]))

```

### 方法2：递归

```python3
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

```


## 10.组合总数
直通车：[https://leetcode-cn.com/problems/combination-sum/](https://leetcode-cn.com/problems/combination-sum/)
```python3
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:

        # 避免重复，将candidates从小到大排序
        candidates = sorted(candidates)

        def trace_back(start, path, temp_sum=0):
            # 递归结束
            if temp_sum == target:
                res.append(path)
                return

            for i in range(start, len(candidates)):
                # 剪枝
                if temp_sum + candidates[i] > target:
                    break
                # 递归下次start包含当前i
                trace_back(i, path + [candidates[i]], temp_sum + candidates[i])

        res = []
        trace_back(0, [])
        return res


# print(Solution().combinationSum(candidates=[2, 3, 6, 7], target=7))
# print(Solution().combinationSum(candidates=[2, 3, 5], target=8))
print(Solution().combinationSum(candidates=[8, 7, 4, 3], target=11))

```


## 11.有重复字符串的排列组合
直通车：[https://leetcode-cn.com/problems/permutation-ii-lcci/](https://leetcode-cn.com/problems/permutation-ii-lcci/)
> 使用回溯+hash_map，其实就是n中选n的问题，一般使用回溯都是遍历n，剔除其中重复的情况，此例使用hash_map保存每个元素以及对应的个数，用于path取值和剪枝，提高效率。

```python3
from typing import List
"""
有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。
"""
# from copy import copy


class Solution:
    def permutation(self, S: str) -> List[str]:
        hash_map = {}
        for i, v in enumerate(S):
            if v in hash_map:
                hash_map[v] += 1
            else:
                hash_map[v] = 1
        res = []
        self.trace_back("", res, len(S), S, hash_map)
        return res

    def trace_back(self, path, res, n, S, hash_map):
        if len(path) == n:
            res.append(path)
            return

        for k in hash_map:
            # 减枝
            if hash_map[k] < 1:
                continue
            hash_map[k] -= 1
            self.trace_back(path + k, res, n, S, hash_map)
            hash_map[k] += 1


print(Solution().permutation("qqe"))
# print(Solution().permutation("ab"))
```

## 12.无重复字符串的排列组合
直通车：[https://leetcode-cn.com/problems/permutation-i-lcci/](https://leetcode-cn.com/problems/permutation-i-lcci/)
> 与有重复字符串的排列组合类似，使用回溯+hash_map，当字符使用过就由True变为False。

```python3
from typing import List


class Solution:
    def permutation(self, S: str) -> List[str]:
        hash_map = {}
        for i, v in enumerate(S):
            if v not in hash_map:
                hash_map[v] = True
        res = []
        self.trace_back("", res, len(S), S, hash_map)
        return res

    def trace_back(self, path, res, n, S, hash_map):
        if len(path) == n:
            res.append(path)
            return

        for k in hash_map:
            if not hash_map[k]:
                continue
            hash_map[k] = False
            self.trace_back(path + k, res, n, S, hash_map)
            hash_map[k] = True


print(Solution().permutation("qwe"))
print(Solution().permutation("ab"))
```

## 13.字符串的排列
直通车：[https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/)

使用回溯法的示意图(不代表本题解体思路，只是为了说明回溯法)
![https://raw.githubusercontent.com/fadeawaylove/article-images/master/ezgif.com-gif-maker.gif](https://raw.githubusercontent.com/fadeawaylove/article-images/master/ezgif.com-gif-maker.gif)


<details>
<summary>查看代码</summary>

```python3
# write your code here.
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        n = len(s)
        visited = [False] * n  # 记录是否被访问的状态
        res = []

        def trace_back(path):
            if len(path) == n:
                res.append(path)
                return
            dic = set()  # 记录同一层中已经使用过的元素
            for i in range(n):  # 一个循环代表一层
                if visited[i]:  # 访问过就剔除
                    continue
                if s[i] in dic:  # 同一层不允许有重复的元素
                    continue
                dic.add(s[i])
                visited[i] = True
                trace_back(path + s[i])
                visited[i] = False

        trace_back("")
        return res


print(Solution().permutation("abc"))
```
</details>

## 14.全排列
直通车：[https://leetcode-cn.com/problems/permutations/](https://leetcode-cn.com/problems/permutations/)

### 方法一：回溯（辅助used列表）

<details>
<summary>查看代码</summary>

```python3
# write your code here.
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        res = []

        def trace_back(path):
            if len(path) == n:
                res.append(path)
                return

            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                trace_back(path + [nums[i]])
                used[i] = False

        trace_back([])
        return res

```
</details>

### 方法二：回溯（交换法）

<details>
<summary>查看代码</summary>

```python3
# write your code here.
"""
使用交换法实现回溯，适合全排列场景
在一层中，first会跟所有range(first,n)范围内的元素都做依次交换，这样正好就展示了当前层的所有情况
"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res
```
</details>

## 15.幂集
直通车：[https://leetcode-cn.com/problems/power-set-lcci/](https://leetcode-cn.com/problems/power-set-lcci/)
### 方法1：回溯

<details>
<summary>回溯</summary>

```python3
# write your code here.
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def trace_back(start, path, total):
            if len(path) == total:
                res.append(path)
                return
            for i in range(start, n):
                trace_back(i+1, path+[nums[i]], total)
        
        for x in range(n+1):
            trace_back(0, [], x)
        return res
```
</details>


### 方法2：递推

<details>
<summary>递推</summary>

```python3
# write your code here.
"""
输入 0 -->[[]]
输入 1 -->[[],[1]]
输入 2 -->[[],[1],[2],[1,2]]
输入 3 -->[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
可以获得 递推公式： f(n) = f(n-1) + [i+[num] for i in f(n-1)]
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [
            [],
        ]
        if not nums:
            return res

        for num in nums:
            res += [arr + [num] for arr in res]
        return res


print(Solution().subsets([1, 2, 3]))

```
</details>


## 16.电话号码的字母组合
直通车：[https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)

![https://raw.githubusercontent.com/fadeawaylove/article-images/master/%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%E7%9A%84%E5%AD%97%E6%AF%8D%E7%BB%84%E5%90%88.gif](https://raw.githubusercontent.com/fadeawaylove/article-images/master/%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%E7%9A%84%E5%AD%97%E6%AF%8D%E7%BB%84%E5%90%88.gif)

<details>
<summary>查看代码</summary>

```python3
# write your code here.
from typing import List


class Solution:
    data = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        n = len(digits)
        res = []

        def trace_back(start, path):
            if len(path) == n:
                res.append(path)
                return
            for i in range(start, n):
                for j in self.data[digits[i]]:
                    trace_back(i + 1, path + j)

        trace_back(0, "")
        return res


print(Solution().letterCombinations("23"))

```
</details>


## 17.子集Ⅱ
直通车：[https://leetcode-cn.com/problems/subsets-ii/](https://leetcode-cn.com/problems/subsets-ii/)
> 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
> 
> 说明：解集不能包含重复的子集。
> 
> 示例:
>
> 输入: [1,2,2]
> 输出:
> [
>   [2],
>   [1],
>   [1,2,2],
>   [2,2],
>   [1,2],
>   []
> ]
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/subsets-ii
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


### 方法1：回溯法
> 其实就是转换为n中选择0到n的问题

<details>
<summary>查看代码</summary>

```python3
# write your code here.
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
```
</details>

### 方法2：递推法

![https://raw.githubusercontent.com/fadeawaylove/article-images/master/87ba90075a0a54e867ee05a65612d6f00766624c9f50f92beb9004e8b5a3ff27-image.png](https://raw.githubusercontent.com/fadeawaylove/article-images/master/87ba90075a0a54e867ee05a65612d6f00766624c9f50f92beb9004e8b5a3ff27-image.png)

> 可以梳理出当前结果和上一个结果之间的关系，f(n) = f(n-1) + (i+[n] for i in f(n-1))，这个式子无法排除重复部分的，但是观察可以得到，重复的都是因为使用了“旧解”，比如上图中，第四行黑色部分重复了，就是因为用了2和第三行绿色部分生成的，如果每次能标记处“旧解”，生成新的下一项解的时候排除掉“旧解”就行了

<details>
<summary>查看代码</summary>

```python3
# write your code here.
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
```
</details>

