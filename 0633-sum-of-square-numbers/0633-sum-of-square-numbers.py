class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        s = 0
        e = int(c ** 0.5)
        while s <= e:
            if s ** 2 + e ** 2 == c:
                return True
            elif s ** 2 + e ** 2 < c:
                s += 1
            else:
                e -= 1
        return False
