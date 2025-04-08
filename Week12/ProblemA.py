from collections import deque

class Graph:
    def __init__(self, v, adj):
        self.vertices = v
        self.adj = adj

    def rescurse(self, vertex, stack, visited):
        visited[vertex] = True
        for u in self.adj[vertex]:
            if not visited[u]:
                self.rescurse(u,stack,visited)
        stack.appendleft(vertex)

    def toposort(self,src):
        visited = [False] * self.vertices
        stack = deque()
        self.rescurse(src, stack, visited)
        if len(stack) != self.vertices:
            return ('back to the lab',)
        for i in range(self.vertices - 1):
            if stack[i + 1] not in self.adj[stack[i]]:
                return ('back to the lab',)
        return stack
            
n,k = map(int, input().split())
edges = [set() for _ in range(n)]
order = set(range(n))
for _ in range(k):
        a,b = map(int,input().split())
        edges[a].add(b)
        order.discard(b)

g = Graph(n, edges)
if len(order) != 1:
        print('back to the lab')
else:
        print(*g.toposort(order.pop()))