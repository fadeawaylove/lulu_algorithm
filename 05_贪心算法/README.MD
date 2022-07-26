
<!-- TOC -->

- [贪心算法](#贪心算法)
    - [1.种花问题](#1种花问题)

<!-- /TOC -->

# 贪心算法
概念：贪心算法（又称贪婪算法）是指，在对问题求解时，总是做出在当前看来是最好的选择。也就是说，不从整体最优上加以考虑，算法得到的是在某种意义上的局部最优解

## 1.种花问题
直通车：[https://leetcode-cn.com/problems/can-place-flowers/](https://leetcode-cn.com/problems/can-place-flowers/)

> 分析：判断一个位置是否能种花，需要满足条件当前位置还没被中过话，并且旁边两个位置也没有种花（边界则只考虑一侧）

```python3
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        count = 0
        m = len(flowerbed)
        if m == 1:
            return flowerbed[0] == 0 and n <= 1

        for i in range(m):
            if flowerbed[i] == 0 and \
            ((m-1> i > 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0) or \
            (i == 0 and flowerbed[1] == 0) or \
            (i == m-1 and flowerbed[m-2] == 0)):
                count += 1
                flowerbed[i] = 1
                if count >= n:
                    return True

        return False
```