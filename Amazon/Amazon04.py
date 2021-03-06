##4 : Brackets in Matrix Chain Multiplication

class Solution:

    def matrixChainOrder(p, n):
        m = [[0 for _ in range(n)] for i in range(n)]
        for l in range (2, n + 1):
            for i in range (n - l + 1):
                j = i + l - 1
                m[i][j] = float('Inf')
                for k in range (i, j):
                    q = (m[i][k] + m[k + 1][j] +(p[i] * p[k + 1] * p[j + 1]))
                    if (q < m[i][j]):
                        m[i][j] = q
                        m[j][i] = k + 1
        
        global result
        result = ""
        def printParenthesis(j, i):
            global result
            if j == i:
                result +=chr(65 + j)
                return
            else:
                result +="("
                printParenthesis(m[j][i] - 1, i)
                printParenthesis(j, m[j][i])
                result +=")"
        for row in m:
            print(row)
        printParenthesis(n - 1, 0)
        return result
