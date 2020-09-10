from typing import List


class Solution:
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.back_trace(0, 9, res, [], k, n)
        return res

    def back_trace(self, start, total, res, path, k, n):
        # 递归跳出条件
        if len(path) == k:
            res.append(path)
            return

        for i in range(start, total):
            # 跳过
            if len(path) == k - 1:
                if sum(path) + self.data[i] != n:
                    continue
            self.back_trace(i + 1, total, res, path + [self.data[i]], k, n)


print(Solution().combinationSum3(3, 7))
print(Solution().combinationSum3(3, 9))
