##8 : Implement Atoi

class Solution:
    def atoi(self,string):
        s = ''
        for i in string:
            
            if 45 <= ord(i) <= 57:
               s = s + i
            else:
                return -1
        return s 
