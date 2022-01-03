##8 : Total Decoding Messages

class Solution:
	def CountWays(self, str):
		# Code here
        def decode(str,i=0,cache={}):
            if i in cache:
                return cache[i]
            if i == len(str):
                return 1
            if int(str[i]) == 0:
                return 0
            count = decode(str, i+1)
            if (i+1 < len(str)) and (int(str[i:i+2]) <= 26):
                count += decode(str, i+2)
            if i not in cache:
                cache[i] = count
            return cache[i]
        return decode(str)
