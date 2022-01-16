##8 : Connect Nodes at Same Level 

from queue import Queue

class Solution:

    def connect(self, root):
        queue = Queue()
        ptr = root
        queue.put(ptr)
        queue.put(None)
        prev = None
        while not queue.empty():
            out = queue.get()
            if out is not None:
                out.nextRight = queue.queue[0]
                prev = out
                if out.left:
                    queue.put(out.left)
                if out.right:
                    queue.put(out.right)
            elif not queue.empty():
                queue.put(None)
        return root
