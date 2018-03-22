import collections
class Solution:
    
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need, missing, i, L = collections.Counter(t), len(t), 0, []
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                L.append((i, j))
        L = sorted(L, key=lambda s: s[1] - s[0]) or [[0,0]]
        return s[L[0][0]:L[0][1]]

s = Solution()
print(s.minWindow("AAA", 'AA'))