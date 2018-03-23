import re
from scipy.special import comb
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.strip() == '' or not re.match(r'^[1-9]*$', re.sub('[12]0', '', s)):
            return 0
        num = 1
        for i in range(0,len(s)-1):
            v = s[i]
            if v == '1' and 0 < int(s[i+1]) and not s[i+2:].startswith('0'):
                num += 1
            if v == '2' and 0 < int(s[i+1]) < 7:
                num += 1
        return num

s = Solution()
print(s.numDecodings("15151515"))

'''1 2 1 2
12 1 2
1 21 2
1 2 12
12 12

1 1 5
1 15
11 5

1 5 1 5 1 5 1 5
15 1 5 1 5 1 5
1 5 15 1 5 1 5
1 5 1 5 15 1 5
1 5 1 5 1 5 15

1 5 15 1 5 15
15 15 1 5 1 5

3 + 2 + 1
3 + 1
1

115

1 '''