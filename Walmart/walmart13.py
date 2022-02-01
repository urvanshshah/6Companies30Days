## 13 : Find the Kth Largest Integer in the Array

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return str(( sorted(nums, key= lambda p:int(p)) )[-k])
