"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
贪心算法思路
1.找子序列的时候，我们希望递增的越慢越好，所以每次上升子序列的那个书越小越好
2.维护一个数组d[i]，表示长度为i的最长上升子序列末尾元素的最小值，len记录目前最长的上升子序列的长度
举例如果有序列[0,4,2]，那么d=[0,2]，表示长度为2的上升子序列末尾为2（而不是4）！！！
举例如果有序列[5,4,2]，那么d=[2]，表示长度为1的上升子序列末尾为2（而不是5）！！！
变化过程如下：
    5 -> d = [5]
    4 -> d = [4]，找到序列中第一个小于4的位置，发现没有，则直接替换d[0]=4
    2 -> d = [2]，同理
3.归纳一下就是：首先d[0]=nums[0]，这是初始状态，然后依次遍历nums，
    如果当前nums[i]>d[-1]，那么d直接末尾插入nums[i]
    如果当前nums[i]<d[-1]，找到nums[i]应该在d中的位置，替换那个位置上的元素（基于d是单调递增的，可以使用二分法查找）

"""

from typing import List


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


# print(Solution().lengthOfLIS([4, 10, 4, 3, 8, 9]))
# print(Solution().lengthOfLIS([0, 8, 4, 12, 2]))
print(Solution().lengthOfLIS([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]))
