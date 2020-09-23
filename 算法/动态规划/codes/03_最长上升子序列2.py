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
                d[l] = nums[
                    i]  # 最后取得左值，是因为d中必定存在一个数大于等于nums[i]，r代表的数是>=nums[i]的，因为只有l=mid+1，最后退出的时候肯定是d[l]>=nums[i]，即d[l]是第一个大于等于nums[i]的数
        return len(d)


# print(Solution().lengthOfLIS([4, 10, 4, 3, 8, 9]))
# print(Solution().lengthOfLIS([0, 8, 4, 12, 2]))
print(Solution().lengthOfLIS([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]))
