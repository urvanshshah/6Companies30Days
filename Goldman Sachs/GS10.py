## 10 : Find max 10 numbers in a list having 10M entries

import heapq

def maxNumbers(nums, n):
    heap = []

    for i in nums:
        heapq.heappush(heap,i)
        
    print(heap)
    return heapq.nlargest(n,nums)

print(maxNumbers([3,5,4,7,92,24,1,32,65,742,23,44,7,89,3,2,2,654,7,66],5))
