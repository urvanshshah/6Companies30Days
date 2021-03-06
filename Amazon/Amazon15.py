## 15 : Delete N nodes after M nodes of a linked list

'''
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def skipMdeleteN(self, head, M, N):
        curr=head
        while(curr):
            for i in range(1,M):
                if curr==None:
                    return
                curr=curr.next
            if curr==None:
                return
            nextNode=curr.next
            for i in range(1,N+1):
                if nextNode==None:
                    # return
                    break
                nextNode=nextNode.next
            curr.next=nextNode
            curr=nextNode
            
        return head
    
