## 14 : Smallest range in K lists

import heapq
class Solution:
    def smallestRange(self, KSortedArray, n, k):
        # code here
        # print the smallest range in a new line
        minheap=[]
        maxx=-float('inf')
        for i in range(k):
            heapq.heappush(minheap,(KSortedArray[i][0],i,0))
            maxx=max(KSortedArray[i][0],maxx)
        heapq.heapify(minheap)
        diff=maxx-minheap[0][0]
        ans=[minheap[0][0],maxx]
       
        while True:
            mini,r,c=heapq.heappop(minheap)
            if diff>maxx-mini:
                diff=maxx-mini
                ans=[mini,maxx]
            if c+1>=len(KSortedArray[r]):
                break
            num=KSortedArray[r][c+1]
            maxx=max(maxx,num)
            heapq.heappush(minheap,(num,r,c+1))
        return ans
