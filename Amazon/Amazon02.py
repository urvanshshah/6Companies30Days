##2 : Longest Mountain

def longestMountain(arr):
    n = len(arr)
    i = 1
    start = 0
    maxLength = 0
    while i<n:
        start=i-1
        top = start
        while i<n and (arr[i]>arr[i-1]):
            top=i
            i+=1
        
        if i==n or i==start+1:
            i+=1
            continue
        
        while i<n and (arr[i]<arr[i-1]):
            i+=1
        
        i-=1
        if i==top:
            i+=1
            continue
        if i-start+1>maxLength:
            maxLength = i-start+1
    
    return maxLength 
