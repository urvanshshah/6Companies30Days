## 10 : Stickler Thief 

class Solution:  
    def FindMaxSum(self,a, n):
        if n == 0:
            return 0
        if n == 1:
            return a[0]
        if n == 2:
            return max(a[0], a[1])
        dp = [0]*n
        dp[0] = a[0]
        dp[1] = max(a[0], a[1])
        for i in range(2, n):
            dp[i] = max(a[i]+dp[i-2], dp[i-1])
        return dp[-1]
