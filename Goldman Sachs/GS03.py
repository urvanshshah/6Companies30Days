##3 : Count the subarrays having product less than k

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        c = 0
        for i in range(0, n):
            if a[i] < k:
                c += 1
            m = a[i]
            for j in range(i + 1, n):
                m = m * a[j]
                if m < k:
                    c += 1
                else:
                    break
        return c
