<!-- TOC -->

- [数组](#数组)
    - [1.形成两个异或相等数组的三元组数目](#1形成两个异或相等数组的三元组数目)
        - [方法1：O(N^2)](#方法1on^2)
        - [方法2：O(N)](#方法2on)

<!-- /TOC -->

# 数组
> 数组是在程序设计中，为了处理方便， 把具有相同类型的若干元素按有序的形式组织起来的一种形式。      
首先，数组会利用 索引 来记录每个元素在数组中的位置，且在大多数编程语言中，索引是从 0 算起的。我们可以根据数组中的索引，快速访问数组中的元素。事实上，这里的索引其实就是内存地址。      
在具体的编程语言中，数组的实现方式具有一定差别。比如 C++ 和 Java 中，数组中的元素类型必须保持一致，而 Python 中则可以不同。相比之下，Python 中的数组（称为 list）具有更多的高级功能。

## 1.形成两个异或相等数组的三元组数目
直通车：[https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/](https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/)

### 方法1：O(N^2)
> 分析：a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]，b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]，要找到a==b成立的三元组(i,j,k)，根据异或结合律,a==b等同于a^b=0，即arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]^arr[j] ^ arr[j + 1] ^ ... ^ arr[k] = 0，也就是再i和k之间找到长度大于等于2的子数组，将这个字数组拆分成两个子数组就可以满足条件，子数组能拆分成k-i个字数组，k-i就是个数。

```python3
from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0
        for i in range(n - 1):
            temp = arr[i]
            for j in range(i + 1, n):
                temp = temp ^ arr[j]
                if temp == 0:
                    count += j - i
        return count
```

### 方法2：O(N)
- 条件1：a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
- 条件2：b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
- 要求解：a==b，分析可知如果a=b，即a^b=0，展开可得arr[i] ^ ... ^ arr[k] = 0，等式两边都亦或上0到i-1，变为arr[0]^...^arr[k]=0^arr[0]^arr[i-1]=arr[0]^arr[i-1]
- 结论：定义一个函数f(x)=arr[0]^...^a[x]，那么只要找到f(k)==f(i-1)，此时下标i-1和k就满足条件，其中的j就是i到k之间的任意值，所以j有k-i+1种可能。

```python3
from typing import List
from collections import defaultdict


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        hash_map = defaultdict(list)  # 累亦或的value:对应的下标列表
        hash_map[0].append(-1)  # value为0的第一个下标定义为-1

        xor = 0
        for i, v in enumerate(arr):
            xor ^= v
            hash_map[xor].append(i)
        print(hash_map)

        ans = 0
        for index_list in hash_map.values():
            for index in range(len(index_list)):
                i = index_list[index] + 1
                for k in index_list[index + 1:]:
                    ans += k - i
        return ans
```








