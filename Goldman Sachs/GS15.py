## 15 : Array Pair Sum Divisibility Problem

from collections import defaultdict
class Solution:
    def canPair(self, nuns, k):
        if (n & 1):
            return 0
        freq = defaultdict(lambda: 0)
        for i in range(0, n):
            freq[((nuns[i] % k) + k) % k] += 1
        for i in range(0, n):
            rem = ((nuns[i] % k) + k) % k
            if (2 * rem == k):
                if (freq[rem] % 2 != 0):
                    return 0
            elif (rem == 0):
                if (freq[rem] & 1):
                    return 0
            elif (freq[rem] != freq[k - rem]):
                return 0
        return 1
