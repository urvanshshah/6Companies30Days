## 12 : Leaders in an array

class Solution:
    def leaders(self, A, N):
        sm=A[-1]
        lst=[A[-1]]
        for j in range(N-2,-1,-1):
            if A[j]>=sm:
                sm=A[j]
                lst.append(A[j])
        return lst[::-1]
