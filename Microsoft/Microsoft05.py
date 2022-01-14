##5 : Stock span problem 

class Solution:
    def calculateSpan(self, a, n):
        st = []
        def helper(price):
            if not st:
                st.append((price,1))
                return 1
            else:
                ans = 1
                while st and st[-1][0]<=price:
                    t = st.pop()
                    ans+=t[1]
                st.append((price,ans))
            return ans
        
        res = []
        for i in range(n):
            res.append(helper(a[i]))
        return res     

