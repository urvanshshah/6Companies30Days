## 12 : Find All Four Sum Numbers

class Solution:
    def fourSum(self, arr, k):
        # code here
        n = len(arr)
        arr.sort()
        result = []
        
        for i in range(n-3):
            for j in range(i+1,n-2):
                l = j+1
                r = n-1
                while (l<r):
                    add = arr[i]+arr[j]+arr[l]+arr[r]
                    if add==k:
                        result.append([arr[i],arr[j],arr[l],arr[r]])
                        l+=1
                        r-=1
                    elif add<k:
                        l+=1
                    else:
                        r-=1
    
        return result
