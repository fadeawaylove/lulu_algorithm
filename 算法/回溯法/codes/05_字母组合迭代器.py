class CombinationIterator:
    """
        其实就是一个n中选k，使用回溯法
    """
    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        ret = []
        self.dfs(0, [], ret, len(characters), combinationLength)
        self.ret = ret
        self.cur = -1

    def dfs(self, start, path, ret, n, k):
        if len(path) == k:
            ret.append("".join(path))
            return

        for i in range(start, n):
            path.append(self.characters[i])
            self.dfs(i + 1, path[:], ret, n, k)
            path.pop()

    def next(self) -> str:
        if self.hasNext():
            self.cur += 1
            return self.ret[self.cur]

    def hasNext(self) -> bool:
        if self.cur + 1 >= len(self.ret):
            return False
        return True


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
obj = CombinationIterator("abc", 2)

print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
