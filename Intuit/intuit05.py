##5 : Split Array Largest Sum

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        start, end = max(nums), sum(nums)
        while start < end:
            mid = start + ((end - start)//2)
            
            summ, count = 0, 1
            for i in range(len(nums)):
                if summ + nums[i] > mid:
                    summ = nums[i]
                    count += 1
                else:
                    summ += nums[i]
                    
            if count <= m:
                end = mid
            else:
                start = mid + 1
        return end
