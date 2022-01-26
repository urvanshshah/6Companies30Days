##5 : Transform to Sum Tree

class Solution:
    #Complete this function
    def power(self,N,R):
        #Your code here
        return self.recurcivePower(N,R) % 1000000007

    def recurcivePower(self,N,R):
        if R == 0:
            return 1
        result = self.power(N,R//2)
        result = (result * result ) % 1000000007
        if R % 2 == 0:
            return result
        return result * N
