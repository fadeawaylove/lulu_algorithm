from typing import List


class Solution:
    def permutation(self, S: str) -> List[str]:
        hash_map = {}
        for i, v in enumerate(S):
            if v not in hash_map:
                hash_map[v] = True
        res = []
        self.trace_back("", res, len(S), S, hash_map)
        return res

    def trace_back(self, path, res, n, S, hash_map):
        if len(path) == n:
            res.append(path)
            return

        for k in hash_map:
            if not hash_map[k]:
                continue
            hash_map[k] = False
            self.trace_back(path + k, res, n, S, hash_map)
            hash_map[k] = True


print(Solution().permutation("qwe"))
print(Solution().permutation("ab"))
