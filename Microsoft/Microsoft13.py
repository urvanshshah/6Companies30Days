## 13 : Bridge edge in a graph

from queue import Queue
class Solution:
    def isBridge(self, V, adj, c, d):
        try:
            adj[c].remove(d)
        except:
            return 0
        try:
            adj[d].remove(c)
        except:
            return 0
        visited = set()
        queue = Queue()
        queue.put(c)
        while not queue.empty():
            out = queue.get()
            visited.add(out)
            for neighbour in adj[out]:
                if neighbour not in visited:
                    queue.put(neighbour)
        if d not in visited:
            return 1
        return 0
