## 1 : Calculating Maximum Profit (Multiple Ladders Question)

class Solution:
    def maxProfit(self, K, N, A):
        if not len(A):
            return 0
        
        profit=[[0 for d in A] for t in range(K+1)]
        # print(profit)
        
        for t in range(1,K+1):
            maxSoFar=float('-inf')
            
            for d in range(1,N):
                maxSoFar=max(maxSoFar,profit[t-1][d-1]-A[d-1])
                profit[t][d]=max(profit[t][d-1],A[d]+maxSoFar)
                
        return profit[-1][-1]
