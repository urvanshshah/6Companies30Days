##4 : Partition Equal Subset Sum

class Solution:
    def equalPartition(self, n, arr):
        # code here
        arrSum = sum(arr)
        if arrSum % 2 != 0:
            return False
            
        #same as subset sum to k problem from here 
        #i.e knapsack variant
           
        else:
            target = arrSum // 2
            dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
            for i in range(n+1):
                for j in range(target+1):
                    if i == 0:
                        dp[i][j] = False
                    if j == 0:
                        dp[i][j] = True
                        
            for i in range(1,n+1):
                for j in range(1,target+1):
                    if arr[i-1] <= j:
                        dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
    
                    else:
                        dp[i][j] = dp[i-1][j]
    
        return dp[n][target]
