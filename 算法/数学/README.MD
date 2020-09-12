
<!-- TOC -->

- [数学方法](#数学方法)
    - [第k个排列](#第k个排列)

<!-- /TOC -->
# 数学方法

## 第k个排列
直通车：[https://leetcode-cn.com/problems/permutation-sequence/](https://leetcode-cn.com/problems/permutation-sequence/)


<details>
<summary>查看代码</summary>

```python3
"""
使用数学方法，关键就是确定是第几个子树
n=3,k=3时
x=2
1) 2!=2, x,y = 2//2, 2%2,得x=1,y=0，第二棵树的子树
2) 2!=2，x,y = 0//2, 0%2,得x=0,y=0，第一颗树的子树
3）1!=1, x,y = 1//1, 1%1,得x=0,y=0，第二棵树的子树

"""


class Solution:
    fact_map = {}

    def getPermutation(self, n: int, k: int) -> str:
        res = ""
        data = [str(i) for i in range(1, n + 1)]
        x = k - 1
        for i in range(n - 1, 0, -1):
            x, y = x // self.get_factorial(i), x % self.get_factorial(i)
            res += (data.pop(x))
            x = y
        res += (data.pop(0))
        return res

    def get_factorial(self, x):
        if x == 0:
            if x not in self.fact_map:
                self.fact_map[x] = 1
            return 1
        ret = x * self.get_factorial(x - 1)
        if x not in self.fact_map:
            self.fact_map[x] = ret
        return ret


print(Solution().getPermutation(4, 9))
print(Solution().getPermutation(9, 296662))
print(Solution().getPermutation(3, 1))
```

</details>