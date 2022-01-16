##2 : Prerequisite Tasks

class Solution:
    def isPossible(self, N, prerequisites):
        #code here
        def dfs(i):
            lst[i] = 1
            if i in graph:
                for j in graph[i]:
                    if lst[j] == 0:
                        if not dfs(j):
                            return False
                    elif lst[j] == 1:
                        return False
            lst[i] = 2
            return True
                            
        graph = {}
        for pair in prerequisites:
            if pair[1] in graph:
                graph[pair[1]].add(pair[0])
            else:
                graph[pair[1]] = set([pair[0]])			
        lst = [0]*N
        for i in range(N):
            if lst[i] == 0:
                if not dfs(i):
                    return False
        return True
