##3 : IPL 2021 - Match Day 2

class Solution:
    def max_of_subarrays(self,arr,n,k):
        
        if n == 1:
            return arr
        a = []
        for i in range(n):
            b = arr[i:k+i]
            if len(b) == k:
                a.append(max(b))
            else:
                break
        return a 
