"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной
Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)
"""

from collections import deque


class Graph:

    def __init__(self, E):
        self.E = E
        self.len = len(E)
        self.bfs_vertex_list = []
        self.vertex_set = set()
        self.queue = deque()
        self.index = -1

        # find first vertex which has neigh(s)
        vertexes = set(self.E)
        while not self.bfs_vertex_list:
            vertex = vertexes.pop()
            # if has neigh(s)
            if self.E[vertex]:
                self.bfs_vertex_list.append(vertex) # add vertex to ordered list
                self.queue.extend(self.E[vertex]) # add neigh(s) to queue

        # make full bfs_vertex_list
        while len(self.bfs_vertex_list) < self.len:
            vertex = self.queue.popleft()
            self.queue.extend(self.E[vertex])
            if vertex not in self.bfs_vertex_list:
                self.bfs_vertex_list.append(vertex)

    def __next__(self):
        if self.index + 1 >= self.len:
            return StopIteration
        self.index += 1
        return self.bfs_vertex_list[self.index]

    def __iter__(self):
        return iter(self.bfs_vertex_list)


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)

for vertex in graph:
    print(vertex)
