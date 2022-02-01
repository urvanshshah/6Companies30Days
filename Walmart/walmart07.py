## 7 : Sorted subsequence of size 3

class Solution:
    def find3number(self,A, n):
        # code here
        stack, result = [], []
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= A[i]:
                stack.pop()
            stack.append(A[i])
            if len(stack) == 3:
                break
        if len(stack) >= 3:
            for i in range(2, -1, -1):
                result.append(stack.pop())
        return result
