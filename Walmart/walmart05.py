##5 : Transform to Sum Tree

class Solution:
    def toSumTree(self, root) :
        #code here
        if(root == None):
            return 0
        old_val = root.data
        root.data = self.toSumTree(root.left) + self.toSumTree(root.right)
        return root.data + old_val
