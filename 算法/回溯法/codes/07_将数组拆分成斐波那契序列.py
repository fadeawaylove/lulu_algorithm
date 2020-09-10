from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        ret = []
        self.dfs(0, len(S), [], S, ret)
        if ret:
            return [int(x) for x in ret[0]]
        return ret

    def dfs(self, start, n, path, s, ret):
        if start == n and len(path) > 2:
            ret.append(path)
            return

        for i in range(start, n):
            temp = s[start:i + 1]
            # 跳过
            if len(path) >= 2:
                if not self.check(path[-2], path[-1], temp):
                    continue
            # 剪枝
            if (temp.startswith("0") and temp != "0") or int(temp) > 2 ** 31 - 1:
                return
            self.dfs(i + 1, n, path[:] + [temp], s, ret)

    def check(self, astr, bstr, cstr):
        if int(astr) + int(bstr) == int(cstr):
            return True
        return False


print(Solution().splitIntoFibonacci("123456579"))
print(Solution().splitIntoFibonacci("1101111"))
print(Solution().splitIntoFibonacci("0123"))
print(Solution().splitIntoFibonacci(
    "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"))
