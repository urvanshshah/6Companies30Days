## 9 : Given a pattern containing only I's and D's. I for increasing and D for decreasing.Devise an algorithm to print the minimum number following that pattern.

from collections import deque
class Solution:
    def printMinNumberForPattern(ob,S):
        if not S or not len(S):
            return S
        result = ''
        stack = deque()
        for i in range(len(S) + 1):
            stack.append(i + 1)
            if i == len(S) or S[i] == 'I':
                while stack:
                    result += str(stack.pop())
        return result
