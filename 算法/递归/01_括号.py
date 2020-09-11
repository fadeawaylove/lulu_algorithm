from typing import List


class Solution:
    # 有时候if可以用and代替，and有条件截断的效果
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def f(l, r, s):
            # 左右括号都达到n，才会执行将结果加到ans中
            l == r == n and ans.append(s)
            # 如果左括号数量小于n，s加上一个左括号，继续递归
            l < n and f(l + 1, r, s + '(')
            # 如果右括号数量小于左括号，s加上一个右括号，继续递归
            r < l and f(l, r + 1, s + ')')

        f(0, 0, '')
        return ans


print(Solution().generateParenthesis(3))
