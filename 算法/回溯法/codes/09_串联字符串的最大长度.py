from typing import List


class Solution:
    def __init__(self):
        self.res = 0

    def maxLength(self, arr: List[str]) -> int:

        for i in range(1, len(arr) + 1):
            self.trace_back(0, [], arr, i)
        return self.res

    def trace_back(self, start, path, arr, k):
        # 结束条件
        if len(path) == k:
            self.res = max(self.res, len("".join(path)))
            return

        for i in range(start, len(arr)):
            if not self.check_single(arr[i]):
                continue
            if len(path) >= 1:
                if not self.check_multiple(path, arr[i]):
                    continue
            self.trace_back(i + 1, path + [arr[i]], arr, k)

    def check_multiple(self, origin_str, target_str):
        origin_str = "".join(origin_str)
        return self.check_single(origin_str + target_str)

    def check_single(self, a_str):
        return len(set(a_str)) == len(a_str)


# print(Solution().maxLength(["jnfbyktlrqumowxd", "mvhgcpxnjzrdei"]))
print(Solution().maxLength(["yy","bkhwmpbiisbldzknpm"]))
