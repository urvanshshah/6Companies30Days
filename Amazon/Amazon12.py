## 12 : Column name from a given column number

class Solution:
    def colName (self, n):
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if n <26:
           return alpha[n-1]
        else:
            q,r = n//26 ,n%26
            
            if r==0:
                if q ==1:
                    return alpha[r-1]
                else:
                    return self.colName(q-1) + alpha[r-1]
            else:
                return self.colName(q) + alpha[r-1]
