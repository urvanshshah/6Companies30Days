## 14 : Minimum steps to destination

class Solution:
    def minSteps(self, D):
        i = 1
        def select(sum,i,count):
            if sum>D or sum<-D:
                return 1e7
            if sum==D:
                return count
            count += 1
            return min(select(sum-i,i+1,count),select(sum+i,i+1,count))
        return select(0,i,0)
    
    def minSteps2(D):
        target = abs(D)
        step = 0
        sum = 0
        
        while sum<target or (sum-target)%2!=0:
            step+=1
            sum += step
        
        return step
