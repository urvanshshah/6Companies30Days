## 1: Subarray with given sum 

class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        i=0
        j=1
        lst=[]
        if arr[0]==s:
            lst=[1,1]
            return lst
        sm=arr[i]
        
        while j<n:
            sm+=arr[j]
            if sm==s:
                lst.append(i+1)
                lst.append(j+1)
                return lst
            if sm>s:
                while sm>s:
                    sm-=arr[i]
                    i+=1
                    if sm==s:
                        lst=[i+1,j+1]
                        return lst
            j+=1
        lst.append(-1)
        return lst
