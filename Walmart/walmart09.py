## 9 : Guess Number Higher or Lower II

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        new=[[0 for i in range(0,n+1)] for i in range(0,n+1)]
        for gap in range(1,n+1):
            for j in range(gap,n+1):
                i=j-gap
                if gap==1:
                    new[i][j]=min(i,j)
                    continue
                if i==0 or j==0:
                    continue
                mini=8765432
                for k in range(i,j+1):
                    if k==i:
                        ans=i+new[i+1][j]
                    elif k==j:
                        ans=j+new[i][j-1]
                    else:
                        ans=k+max(new[k+1][j],new[i][k-1])
                    mini=min(ans,mini)
                new[i][j]=mini
        print(new)
        return new[1][-1]
