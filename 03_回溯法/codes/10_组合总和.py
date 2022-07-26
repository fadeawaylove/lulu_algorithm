from typing import List


class Solution:
    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:

        # 避免重复，将candidates从小到大排序
        candidates = sorted(candidates)

        def trace_back(start, path, temp_sum=0):
            # 递归结束
            if temp_sum == target:
                res.append(path)
                return

            for i in range(start, len(candidates)):
                # 剪枝
                if temp_sum + candidates[i] > target:
                    break
                # 递归下次start包含当前i
                trace_back(i, path + [candidates[i]], temp_sum + candidates[i])

        res = []
        trace_back(0, [])
        return res


# print(Solution().combinationSum(candidates=[2, 3, 6, 7], target=7))
# print(Solution().combinationSum(candidates=[2, 3, 5], target=8))
print(Solution().combinationSum(candidates=[8, 7, 4, 3], target=11))
