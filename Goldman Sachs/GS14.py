## 14 : Minimum Size Subarray Sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        result = 0
        length = len(nums)+1
        for j in range(len(nums)):
            result += nums[j]
            while result>=target:
                    if length > j-i+1:
                        length = j-i+1
                        if length==1:
                            return 1
                    result -= nums[i]
                    i+=1

        return length if length!=len(nums)+1 else 0
