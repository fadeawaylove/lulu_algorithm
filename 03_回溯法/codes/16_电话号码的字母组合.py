from typing import List


class Solution:
    data = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        n = len(digits)
        res = []

        def trace_back(start, path):
            if len(path) == n:
                res.append(path)
                return
            for i in range(start, n):
                for j in self.data[digits[i]]:
                    trace_back(i + 1, path + j)

        trace_back(0, "")
        return res


print(Solution().letterCombinations("23"))
