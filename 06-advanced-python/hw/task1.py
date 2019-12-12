"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной
Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)
"""

from collections import deque


def bfs(graph, start):
    bfs_seq = [start]
    queue = deque(graph[start])
    for i in range(len(graph)):
        if queue:
            vertex = queue.popleft()
            bfs_seq.append(vertex)
            neighs = graph[vertex]
            for neigh in neighs:
                if neigh not in bfs_seq:
                    if neigh not in queue:
                        queue.append(neigh)
        else:
            # graph is not reachable
            break
    return bfs_seq


class Graph:

    def __init__(self, E):
        self.E = E
        self.len = len(E)
        self.index = -1
        self.bfs_list = self.bf_search()

    def bf_search(self):
        self.vertexes = set(self.E.keys())
        self.queue = deque()
        self.bfs = []
        # find first vertex from which we can reach all other vertexes
        while self.vertexes:
            start_vertex = self.vertexes.pop()
            self.bfs = bfs(self.E, start_vertex)
            if len(self.bfs) == self.len:
                return self.bfs
        else:
            print('Can not reach end of graph from any vertex')
        return self.bfs

    def __next__(self):
        if self.index + 1 >= self.len:
            raise StopIteration
        self.index += 1
        return self.bfs_list[self.index]

    def __iter__(self):
        return self


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}


graph = Graph(E)

for vertex in graph:
    print(vertex)
