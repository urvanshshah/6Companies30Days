##8 : Maximum Height Tree

class Solution:
    def height(self, N):
        # code here
        i, res = 1, 1
        while res <= N:
            res += i+1
            i += 1
        return i-1
