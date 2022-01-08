## 7 : First non-repeating character in a stream

from queue import Queue
class Solution:
	def FirstNonRepeating(self, A):
		# Code here
    	visited = {}
        noRepeatingChar = Queue()
        noRepeatingChar.put(A[0])
        result = ''
        for char in A:
            if char in visited:
                visited[char] +=1
                replace = '#'
                while not noRepeatingChar.empty():
                    if visited[noRepeatingChar.queue[0]] >1:
                        noRepeatingChar.get()
                    else:
                        replace = noRepeatingChar.queue[0]
                        break
                result += replace
                continue
            
            visited[char] = 1
            noRepeatingChar.put(char)
            result += noRepeatingChar.queue[0]
            
        return result
