## 13 : Minimum operations to convert array A to B

import bisect
class Solution:
    def binary_search(self,arr2,n,m):
        low=0
        high=m-1
        while(low <= high):
            mid=low+(high-low)//2
            if (arr2[mid] == n):
                return True
            elif (arr2[mid] > n):
                high=mid-1
            else:
                low=mid+1
        return False
    def minInsAndDel(self, arr1, arr2, n, m):
        binary=[]
        for i in range(n):
            if (self.binary_search(arr2,arr1[i],m)):
                binary.append(arr1[i])
        if (len(binary) == 0):
            return (n+m)
        ans=[]
        ans.append(binary[0])
        for i in range(1,len(binary)):
            if (ans[-1] < binary[i]):
                ans.append(binary[i])
            else:
                ind=bisect.bisect_left(ans,binary[i])
                ans[ind]=binary[i]
        return ((n+m)-2*(len(ans)))
