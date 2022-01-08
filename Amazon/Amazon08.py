##8 : Count ways to N'th Stair(Order does not matter)

import math

class Solution:
    def countWays(self,m):
        mod = 1000000007
        n = math.ceil(m//2)
        return (n+1)
