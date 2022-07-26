class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        # 也就是说当前点数为K-1的时候，下一个点数最多为K-1+W，如果K-1+W<=N，那么永远不会输
        if K + W - 1 <= N:
            return 1.0

        dp = [0] * (K + W)
        # 有些点数的概率已知
        for i in range(K, N + 1):
            dp[i] = 1

        sum_pro = N - K + 1
        # 计算K+W这几个数的概率和
        for i in range(K - 1, -1, -1):
            dp[i] = sum_pro / W
            sum_pro = sum_pro + dp[i] - dp[i + W]
        return dp[0]


print(Solution().new21Game(21, 17, 10))
