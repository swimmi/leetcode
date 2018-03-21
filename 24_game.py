import itertools
class Solution:
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ops, eps = ['+', '-', '*', '/'], ['%d%s%d%s%d%s%d','%d%s(%d%s%d)%s%d','(%d%s%d)%s(%d%s%d)','%d%s(%d%s(%d%s%d))','%d%s((%d%s%d)%s%d)','%d%s(%d%s%d%s%d)']
        las, lbs = list(itertools.permutations(nums, len(nums))), list(itertools.product(ops, repeat=3))
        for a in las:
            for b in lbs:
                for e in eps:
                    res = e % (a[0],b[0],a[1],b[1],a[2],b[2],a[3])
                    try:
                        if abs(24 - eval(res)) <= 0.000001:
                            return True
                    except ZeroDivisionError:
                        pass
        return False

s = Solution()
print(s.judgePoint24([6, 7, 8, 1]))