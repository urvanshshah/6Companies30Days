## 6:Given two strings str1 and str2. We say that str2 divides str1 if it's possible

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Create the function that returns set of divisor for each string
        def divisor(s):
          factor = ''
          divisor = []
          for i in s:
             factor+=i
             if s == factor*(len(s)//len(factor)):
                 divisor.append(factor)
          return set(divisor)

        divisor1 = divisor(str1)
        divisor2 = divisor(str2)
        # Find the common divisors for both the strings
        result = list(divisor1.intersection(divisor2))
        # sort the above list by the length of each divisor
        final_result = sorted(result, key = lambda x : len(x))
        if final_result :
            return final_result[-1]
        else:
            return ""
