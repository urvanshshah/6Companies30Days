## 7 : Distributing M items in a circle of size N starting from K-th position

def lastPosition(n, m, k):
    return (k + (m % n) -1)

n = int(input())  #5
m = int(input())  #8
k = int(input())  #2
print(lastPosition(n, m, k))  #4
