from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        n = len(s)
        visited = [False] * n  # 记录是否被访问的状态
        res = []

        def trace_back(path):
            if len(path) == n:
                res.append(path)
                return
            dic = set()  # 记录同一层中已经使用过的元素
            for i in range(n):  # 一个循环代表一层
                if visited[i]:  # 访问过就剔除
                    continue
                if s[i] in dic:  # 同一层不允许有重复的元素
                    continue
                dic.add(s[i])
                visited[i] = True
                trace_back(path + s[i])
                visited[i] = False

        trace_back("")
        return res


print(Solution().permutation("abc"))
