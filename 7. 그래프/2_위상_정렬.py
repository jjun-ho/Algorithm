class Graph():
    def __init__(self, vertices):
        self.V = vertices  # 정점 수
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]  # 각 정점이 향할 수 있는 정점
        self.visited = [False] * self.V  # 모든 정점 visited False로 초기화
        self.R = []  # 리스트 R

    def TOPOLOGICAL_SORT(self):
        for v in range(len(self.graph)):
            if self.visited[v] == False:
                self.DFS(v)
        self.R.reverse()  # 리스트 R의 맨 앞에 v 추가한 효과

    def DFS(self,v):
        self.visited[v] = True
        for x in range(self.V):
            if self.graph[v][x] == 1:  # 정점 v가 향할 수 있는 정점이라면
                if self.visited[x] == False:
                    self.DFS(x)
        self.R.append(v)  # 리스트 R의 맨 뒤에 v 추가 -> 마지막에 reverse = 리스트 R의 맨 앞에 추가 v 추가
        print(v) # 리스트 R의 맨 앞에 추가되는 정점(v) 무엇인지 print

g = Graph(6)
g.graph = [[0, 1, 0, 0, 0, 0],
           [0, 0, 1, 1, 0, 1],
           [0, 0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 1],
           [0, 0, 0, 1, 0, 0]]  # 각 정점이 향할 수 있는 정점
g.TOPOLOGICAL_SORT()
print(g.R)

"""
* 위상 정렬(Topological Sorting)
- 사이클이 없는 유향 그래프 G=(V, E)에서 모든 정점 정렬
-> 간 (i, j)가 존재하면 정렬 결과에서 정점 i는 j보다 앞에 위치
- 수행 시간: Θ(𝑉 + 𝐸)
"""

"""
# 다른 참고 code
from collections import defaultdict
class Graph:
    #유향 그래프로 생성
    def __init__(self, directed=True):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdge(self, alt, dest):
        self.graph[alt].append(dest)
        if self.directed is False:
            self.graph[dest].append(alt)
        else:
            self.graph[dest] = self.graph[dest]

    def topovisit(self, s, visited, sortlist):
        visited[s] = True
        for i in self.graph[s]:
            if not visited[i]:
                self.topovisit(i, visited, sortlist)
        sortlist.insert(0, s)

    def topoSort(self):
        visited = {i: False for i in self.graph}
        sortlist = []

        for v in self.graph:
            if not visited[v]:
                self.topovisit(v, visited, sortlist)
        print(sortlist)

#main문
if __name__ == '__main__':
    graph1 = Graph()
    graph1.addEdge(1, 2)
    graph1.addEdge(1, 3)
    graph1.addEdge(1, 4)
    graph1.addEdge(2, 5)
    graph1.addEdge(2, 6)
    graph1.addEdge(3, 7)
    graph1.addEdge(3, 8)
    graph1.addEdge(4, 9)

#Sort된 graph1 확인
    graph1.topoSort()
"""