## 12 : Find total number of Squares in a N*N chessboard

def countSquares(n):
	return ((n * (n + 1) / 2)* (2 * n + 1) / 3)

n = int(input())
print(countSquares(n))
