

# 数组
> 数组是在程序设计中，为了处理方便， 把具有相同类型的若干元素按有序的形式组织起来的一种形式。      
首先，数组会利用 索引 来记录每个元素在数组中的位置，且在大多数编程语言中，索引是从 0 算起的。我们可以根据数组中的索引，快速访问数组中的元素。事实上，这里的索引其实就是内存地址。      
在具体的编程语言中，数组的实现方式具有一定差别。比如 C++ 和 Java 中，数组中的元素类型必须保持一致，而 Python 中则可以不同。相比之下，Python 中的数组（称为 list）具有更多的高级功能。

## 1.形成两个异或相等数组的三元组数目
直通车：[https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/](https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/)

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






