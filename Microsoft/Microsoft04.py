##4 : Spirally traversing a matrix

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        # code here
        left = top = 0
        right = c-1
        down = r-1
        spiral = []
        dire = 0
        
        while top <= down and left <= right:
            if dire == 0:
                for i in range(left, right+1):
                    spiral.append(matrix[top][i])
                top += 1
                
            elif dire == 1:
                for i in range(top, down+1):
                    spiral.append(matrix[i][right])
                right -= 1
                
            elif dire == 2:
                for i in range(right, left-1, -1):
                    spiral.append(matrix[down][i])
                down -= 1
                
            elif dire == 3:
                for i in range(down, top-1, -1):
                    spiral.append(matrix[i][left])
                left += 1
                    
            dire = (dire+1) % 4
                
        return spiral
