from typing import List
"""
有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。
"""
# from copy import copy


class Solution:
    def permutation(self, S: str) -> List[str]:
        hash_map = {}
        for i, v in enumerate(S):
            if v in hash_map:
                hash_map[v] += 1
            else:
                hash_map[v] = 1
        res = []
        self.trace_back("", res, len(S), S, hash_map)
        return res

    def trace_back(self, path, res, n, S, hash_map):
        if len(path) == n:
            res.append(path)
            return

        for k in hash_map:
            if hash_map[k] < 1:
                continue
            hash_map[k] -= 1
            self.trace_back(path + k, res, n, S, hash_map)
            hash_map[k] += 1


print(Solution().permutation("qqe"))
# print(Solution().permutation("ab"))
