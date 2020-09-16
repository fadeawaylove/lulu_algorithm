<!-- TOC -->

- [动态规划](#动态规划)
    - [1.三角形最小路径和](#1三角形最小路径和)
        - [方法1：动态规划](#方法1动态规划)
        - [方法2：动态规划+空间优化](#方法2动态规划空间优化)
    - [2.计算各个位数不同的数字个数](#2计算各个位数不同的数字个数)
    - [3.最长上升子序列](#3最长上升子序列)
        - [方法1：动态规划](#方法1动态规划-1)
        - [方法2：贪心算法+二分法](#方法2贪心算法二分法)

<!-- /TOC -->

# 动态规划
> 动态规划（英语：Dynamic programming，简称 DP）是一种在数学、管理科学、计算机科学、经济学和生物信息学中使用的，通过把原问题分解为相对简单的子问题的方式求解复杂问题的方法。
>
> 动态规划常常适用于有重叠子问题和最优子结构性质的问题，动态规划方法所耗时间往往远少于朴素解法。
>
> 动态规划背后的基本思想非常简单。大致上，若要解一个给定问题，我们需要解其不同部分（即子问题），再根据子问题的解以得出原问题的解。动态规划往往用于优化递归问题，例如斐波那契数列，如果运用递归的方式来求解会重复计算很多相同的子问题，利用动态规划的思想可以减少计算量。
>
> 通常许多子问题非常相似，为此动态规划法试图仅仅解决每个子问题一次，具有天然剪枝的功能，从而减少计算量：一旦某个给定子问题的解已经算出，则将其记忆化存储，以便下次需要同一个子问题解之时直接查表。这种做法在重复子问题的数目关于输入的规模呈指数增长时特别有用。


方法总结：使用状态转移方程，描述中间状态之间的关系，即描述前一个小结果和后一个小结果之间的关系，依据这个关系链依次推导，可以得到最终结果。

适用情形：中间状态（结果）依赖于前一次的状态（结果）

## 1.三角形最小路径和
直通车：[https://leetcode-cn.com/problems/triangle/](https://leetcode-cn.com/problems/triangle/)


### 方法1：动态规划
> 思路分析：关键是获取中间状态之间的关系，根据题意我们可以知道，用f表示计算最短路径函数的话，位置为triangle[i][j]时，最短路径和为f(i,j)=min(f(i-1, j), f(i-1, j-1)) + triangle[i][j]，意思就是当前元素的最短路径和等于相邻上层元素的最短路和中的较小值加上当前位置元素的值（注意边界条件：元素为当前层第一个或者最后一个的时候，相邻的上层元素可以唯一确定）

```python3
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)  # 数组的长度（三角形的高度）
        f = [[0] * n for _ in range(n)]  # 保存每一层的结果，到当前层当前元素的最小路径
        f[0][0] = triangle[0][0]  # 第一层，第一个元素的结果就是三角形顶的值

        # 遍历获取每一层的结果
        for i in range(1, n):
            # 当前是第i行，从第二行（i=1表示第二行）开始
            # 这是边界条件，每一行的第一个元素只能由上一行的第一个元素获得
            f[i][0] = f[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                # 第(i,j)个元素的结果，等于(i-1,j-1)和(i-1, j)中的较小值 加上 (i,j)处原本的值
                f[i][j] = min(f[i - 1][j], f[i - 1][j - 1]) + triangle[i][j]
            # 这是边界条件，每一行的第最后一个元素只能由上一行的最后一个元素获得
            f[i][i] = f[i - 1][i - 1] + triangle[i][i]
        return min(f[n - 1])


print(Solution().minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]))
```

### 方法2：动态规划+空间优化
> 思路分析：上例子中用n*n的二维数组保存了每一层每个元素的结果，但是实际上可以只用一个n维数组就可以做到。当前元素的结果都是由上一层的结果和当前元素的值得到的，我们可以考虑临界情况，因为每一层都比上一层多一个元素，所以如果每一层从最后一个元素遍历，得到最后一个元素的结果，此时并不会改变已经得到的上一层各个元素的结果，再依次往前将上一层的结果经过计算替换成当前层的结果就行了。

|下标（层）|当前状态（结果）|当前层的值|说明|
|---|---|---|---|
|0 |[2, 0, 0, 0] |[2]|第一层只占用了一个位置|
|1 |[5, 6, 0, 0] |[3, 4]||
|2 |[11, 10, 13, 0] |[6, 5, 7]|
|3 |[15, 11, 18, 16] |[4, 1, 8, 3]|

> 举例分析从下标1到2的情况：我们第2层（下标为1）的结果数组r=[5, 6, 0, 0]和第3层（下标为2）的数据源s=[6, 5, 7],想要得到第3层的结果，根据结果中的状态关系（注意临界情况）可得r[2]=r[1]+s[2]=6+7=13，此时r=[5,6,13,0]，可以看到新计算的第3层的最后一个位置的结果并未影响上一层的结果，继续计算r[1]=min(r[1], r[0]) + s[1]=5+5=10，此时r=[5,10,13,0]，
继续计算r[0]=r[0] + s[0]=11，此时r=[11,10,13,0]，与上表中第3层的记过一致。

```python3
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)  # 数组的长度（三角形的高度）
        f = [0] * n  # 保存每一层的结果，到当前层当前元素的最小路径
        f[0] = triangle[0][0]  # 第一层，第一个元素的结果就是三角形顶的值

        # 遍历获取每一层的结果
        for i in range(1, n):
            f[i] = f[i-1] + triangle[i][i]  # 边界条件，f[i]是最后一个元素
            for j in range(i-1, 0, -1):
                # 第(i,j)个元素的结果，等于(i-1,j-1)和(i-1, j)中的较小值 加上 (i,j)处原本的值
                f[j] = min(f[j-1], f[j]) + triangle[i][j]
            # 这是边界条件，每一行的第最后一个元素只能由上一行的最后一个元素获得
            f[0] = f[0] + triangle[i][0]
        return min(f)


print(Solution().minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]))
```

## 2.计算各个位数不同的数字个数
直通车：[https://leetcode-cn.com/problems/count-numbers-with-unique-digits/](https://leetcode-cn.com/problems/count-numbers-with-unique-digits/)

```python3
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """
        n=0时,dp[0]=1
        n=1时,dp[1]=10+dp[0]-1=10
        n=2时,dp[2]=10*9+dp[1]-9=90+10-9=91
        n=3时,dp[3]=10*9*8+dp[2]-9*8=720+91-72=739
        可以得到转移方程dp[n]=10*...*(10-n+1)+dp[n-1]-9*...(10-n+1)=9*9*...*(10-n+1)+dp[n-1]
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            temp = 9
            for m in range(i - 1):
                temp *= 9 - m
            dp[i] = dp[i - 1] + temp
        return dp[-1]


print(Solution().countNumbersWithUniqueDigits(3))
```

## 3.最长上升子序列

> 给定一个无序的整数数组，找到其中最长上升子序列的长度。
>
> 示例:
>
> 输入: [10,9,2,5,3,7,101,18]
>
> 输出: 4
>
> 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
>
> 说明:
>
> 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
>
> 你算法的时间复杂度应该为 O(n2) 。
>
> 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
>
> 来源：力扣（LeetCode）
>
> 链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
>
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

### 方法1：动态规划
![https://raw.githubusercontent.com/fadeawaylove/article-images/master/ezgif-4-91ef687e54a6.gif](https://raw.githubusercontent.com/fadeawaylove/article-images/master/ezgif-4-91ef687e54a6.gif)

解题思路：
> 首先dp[i]表示第i个元素为终点的最长上升子序列的长度，计算dp[i+1]:
> 1. 如果nums[i+1]>nums[i],dp[i+1] = dp[i] + 1;
> 2. 如果nums[i+1]<nums[i]，那么遍历nums[:i]，找到中间满足nums[j]<nums[i+1]中最大的那个,nums[i+1] = max(nums[j]) + 1

<details>
<summary>查看代码</summary>

```python3
# write your code here.
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # print(dp)
        return max(dp)


print(Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
```
</details>

### 方法2：贪心算法+二分法
解题思路：
> 1.找子序列的时候，我们希望递增的越慢越好，所以每次上升子序列的那个书越小越好
> 2.维护一个数组d[i]，表示长度为i的最长上升子序列末尾元素的最小值，len记录目前最长的上升子序列的长度
> 举例如果有序列[0,4,2]，那么d=[0,2]，表示长度为2的上升子序列末尾为2（而不是4）！！！
> 举例如果有序列[5,4,2]，那么d=[2]，表示长度为1的上升子序列末尾为2（而不是5）！！！
> 变化过程如下：
>     5 -> d = [5]
>     4 -> d = [4]，找到序列中第一个小于4的位置，发现没有，则直接替换d[0]=4
>     2 -> d = [2]，同理
> 3.归纳一下就是：首先d[0]=nums[0]，这是初始状态，然后依次遍历nums，
>     如果当前nums[i]>d[-1]，那么d直接末尾插入nums[i]

<details>
<summary>查看代码</summary>

```python3
# write your code here.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        d = [nums[0]]
        for i in range(1, n):
            if nums[i] > d[-1]:
                d.append(nums[i])
            elif nums[i] < d[-1]:
                # 二分查找找到适合的位置替换下,应该是找到第一个大于nums[i]的数，然后替换
                l = 0
                r = len(d) - 1
                while l < r:  # 这里是小于
                    mid = (r + l) >> 1
                    # mid = (r + l) // 2
                    if d[mid] < nums[i]:
                        l = mid + 1
                    else:
                        r = mid
                d[l] = nums[i]  # 最后取得左值，是因为d中必定存在一个数大于等于nums[i]，r代表的数是>=nums[i]的，因为只有l=mid+1，最后退出的时候肯定是d[l]>=nums[i]，即d[l]是第一个大于等于nums[i]的数
        return len(d)
```
</details>
    