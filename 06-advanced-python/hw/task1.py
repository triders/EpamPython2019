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
        # try to find first vertex from which we can reach all other vertexes
        while self.vertexes:
            start_vertex = self.vertexes.pop()
            self.bfs = bfs(self.E, start_vertex)
            if len(self.bfs) == self.len:
                return self.bfs
        else:
            # Can not reach end of graph from any vertex
            # will do it in other way:
            self.vertexes_to_visit = set(self.E.keys())
            start_vertex = self.vertexes_to_visit.pop()
            self.bfs = bfs(self.E, start_vertex)
            self.vertexes_to_visit.difference_update(set(self.bfs))
            while len(self.bfs) != self.len:
                self.bfs_add = bfs(self.E, self.vertexes_to_visit.pop())
                for vertex in self.bfs_add:
                    if vertex not in self.bfs:
                        self.bfs.append(vertex)
        return self.bfs

    def __next__(self):
        if self.index + 1 >= self.len:
            self.index = -1
            raise StopIteration
        self.index += 1
        return self.bfs_list[self.index]

    def __iter__(self):
        return self


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A'], 'E': []}


graph = Graph(E)

for vertex in graph:
    print(vertex)
