## 6:Possible Words From Phone Digits

class Solution:
    
    #Function to find list of all words possible by pressing given numbers.
    def possibleWords(self, a, N):
        #Your code here
        comb = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        
        def check(i, lst):
            if len(lst) == N:
                res.append("".join(lst))
                return
            
            temp = comb[a[i]]
            for t in temp:
                lst.append(t)
                check(i+1, lst)
                lst.pop()
        
        res = []
        check(0, [])
        return res
