## 12 : Winner of an election

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        # Your code here
        # return the name of the winning candidate and the votes he recieved
        dct=dict()
        arr.sort()
        for i in arr:
            if i in dct:
                dct[i]+=1
            else:
                dct[i]=1
        vmx=max(dct.values())
        for i in arr:
            if dct[i]==vmx:
                lst=[i,vmx]
                return lst
