## 6: Maximum of all subarrays of size k

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        maxVal = [0]*n
        maxStart = max(arr[:k])
        
        for i in range(k):
            maxVal[i] = maxStart
        
        for i in range(k,n):
            if arr[i]>maxVal[i-1]:
                for m in range(i-k+1,i+1):
                    maxVal[m] = arr[i]
        
            elif arr[i]==maxVal[i-1]:
                maxVal[i]=maxVal[i-1]
            
            elif arr[i-k]==maxVal[i-1]:
                maximum = max(arr[i-k+1:i+1])
                for m in range(i-k+1,i+1):
                    maxVal[m] = maximum
            else:
                maxVal[i] = maxVal[i-1]
            
        return maxVal[:n-k+1]
