##4 : Given a string, Your task is to  complete the function encode that returns the run length encoded string for the given string.

def encode(arr):
    a = arr[0]
    z = arr[0]
    v = 0
    for c in arr:
        if c==z:
            v+=1
        else:
            a += str(v)
            a += c
            v = 1
        z = c
    a += str(v)
    return a
