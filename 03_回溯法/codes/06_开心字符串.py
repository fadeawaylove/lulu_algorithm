class Solution:
    data = ['a', 'b', 'c']

    def getHappyString(self, n: int, k: int) -> str:
        res = []
        self.dfs(0, n, [], res, k)
        if k > len(res):
            return ""
        return "".join(res[k - 1])

    def dfs(self, start, n, path, res, k):
        if len(path) == n:
            res.append(path)
            return

        for i in self.data:
            # 剪枝
            if path and path[-1] == i:
                continue
            path.append(i)
            self.dfs(0, n, path[:], res, k)
            # 优化，当结果满足k个后，直接返回
            if len(res) >= k:
                return
            path.pop()
