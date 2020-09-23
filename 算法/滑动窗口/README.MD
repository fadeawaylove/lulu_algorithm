<!-- TOC -->

- [滑动窗口](#滑动窗口)
    - [1.最长湍流子数组](#1最长湍流子数组)

<!-- /TOC -->

# 滑动窗口

## 1.最长湍流子数组
![](https://raw.githubusercontent.com/fadeawaylove/article-images/master/%E4%BC%81%E4%B8%9A%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200923145315.png)

<details>
<summary>查看代码</summary>

```python3
# write your code here.
from typing import List
"""
其实就是寻找符合条件的最长子序列
如果1、0、-1分别代表>、=、<，那么序列：[250, 50, 219, 258, 199, 79, 36, 218, 218, 248] 可以转化为:[1, -1, -1, 1, 1, 1, -1, 0, -1]
问题就可以转化为寻找[1, -1, -1, 1, 1, 1, -1, 0, -1]中最长的交替子数组（-1，1，-1或者1，-1，1交替）
[1,-1] [-1,1] [1] [1,-1] [0] [-1]
"""


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        n = len(A)
        ans = 1
        anchor = 0
        for i in range(1, n):
            op = self.cmp(A[i - 1], A[i])
            if i == n - 1 or op * self.cmp(A[i], A[i + 1]) != -1:  # 条件不满足时，更新anchor，代表这一段子串结束
                if op != 0:  # 如果不是等号，可以计算一次ans
                    ans = max(ans, i - anchor + 1)
                anchor = i
        return ans

    def cmp(self, a, b):
        if a == b:
            return 0
        return 1 if a > b else -1


print(Solution().maxTurbulenceSize(
    [250, 50, 219, 258, 199, 79, 36, 218, 218, 248]))
```
</details>