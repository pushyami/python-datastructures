from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFS(self,v,visited):
        visited[v] = True
        print v,

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFS(i,visited)
    def len(self):
        return len(self.graph)

def main():
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print "DFS from vertex 2: "
    visited = [False]*g.len()
    g.DFS(2,visited)

main()
