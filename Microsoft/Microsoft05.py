##5 : Stock span problem 

class Solution:
    def calculateSpan(self,a,n):
        s = []
        for i in range(n):
            c = 1
            j = i-1
            while j>=0 and a[j] <=a[i]:
                c +=1
                j-=1
            s.append(c)    
        return s 
