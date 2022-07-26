class Solution:
    data = ['a', 'b', 'c']

    def getHappyString(self, n: int, k: int) -> str:
        # 长度超出直接返回
        if k > 3 * 2**(n - 1):
            return ""
        base = {"":["a", "b", "c"], "a": ["b", "c"], "b":["a", "c"], "c":["a", "b"]}

        res = ""
        k -= 1
        for i in range(n, 0, -1):
            x, k = k // 2**(i-1), k % 2**(i-1)
            if res:
                res += base[res[-1]][x]
            else:
                res = base[res][x]
        return res


print(Solution().getHappyString(3, 9))