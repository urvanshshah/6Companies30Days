## 13 : Decode the string

class Solution:
    def decodedString(self, s):
        # code here
        stack = []
        currString = ''
        currNum = 0
        
        for c in s:
            if c=='[':
                stack.append(currString)
                stack.append(currNum)
                currString = ''
                currNum = 0
                
            elif c==']':
                num = stack.pop()
                currString = stack.pop() + num*currString
                
            elif c.isdigit():
                currNum = currNum*10+int(c)
            else:
                currString += c
        
        return currString
