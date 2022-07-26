"""
也可以使用动态规划，重点是找到转移方程
"""


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