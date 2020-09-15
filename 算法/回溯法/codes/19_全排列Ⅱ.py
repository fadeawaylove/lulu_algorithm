from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        visited = [False] * n

        def dfs(path):
            if len(path) == n:
                res.append(path)
                return
            dic = set()
            for i in range(n):
                if visited[i]:
                    continue
                if nums[i] in dic:
                    continue
                dic.add(nums[i])
                visited[i] = True
                dfs(path + [nums[i]])
                visited[i] = False

        dfs([])
        return res
