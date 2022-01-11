## 11 : Tree Serialization and Deserialization

def serialize(root, A):
    A.append(root)
    i=0
    while i<len(A):
        if A[i] is None:
            i+=1
            continue
        A.append(A[i].left)
        A.append(A[i].right)
        i+=1
    for i in range(len(A)):
        if A[i] is None:
            print(None)
            continue
        print(A[i].data)
    return A  
def deSerialize(A):
    q = Queue()  
    q.put(A[0])
    root = A[0]
    i=0
    while not q.empty():
        out = q.get()
        out.left = A[i+1]
        out.right = A[i+2]
        if A[i+1] is not None:
            q.put(A[i+1])
        if A[i+2] is not None:    
            q.put(A[i+2])
        i+=2
    return root
