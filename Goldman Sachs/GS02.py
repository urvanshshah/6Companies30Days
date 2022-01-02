##2 : Overlapping rectangles

class Solution:

    def doOverlap(self, L1, R1, L2, R2):
        
        if  R2[1] >L1[1] or R1[1]>L2[1]:
            return 0
        if   L2[0]> R1[0]  or L1[0] > R2[0]:
            return 0
           
        return 1 
