from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []
        if n > 12:
            return res

        def trace_back(start, path):
            # 四段ip
            if len(path) == 4:
                if start == n:  # 遍历完则加入结果，否则直接回溯
                    res.append(".".join(path))
                return

            for i in range(start, n):
                temp = s[start:i + 1]
                # 含有前导0
                if temp != "0" and temp.startswith("0"):
                    return
                # 如果满足0-255之间
                if int(temp) < 0 or int(temp) > 255:
                    return
                trace_back(i + 1, path + [temp])

        trace_back(0, [])
        return res
