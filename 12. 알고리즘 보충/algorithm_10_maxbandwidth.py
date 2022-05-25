# A Python program for Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix representation of the graph

import sys  # Library for INT_MAX


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        print(self.graph)

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def maxKey(self, key, mstSet):

        max= 0
        for v in range(self.V):
            if key[v] > max and mstSet[v] == False:
                max = key[v]
                max_index = v
        return max_index

    def primMST(self):

        key = [0] * self.V
        parent = [None] * self.V
        key[0] = sys.maxsize
        mstSet = [False] * self.V

        parent[0] = -1

        for cout in range(self.V):

            u = self.maxKey(key, mstSet)

            mstSet[u] = True
            print(mstSet)

            for v in range(self.V):

                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] < min(key[u], self.graph[u][v]):
                    key[v] =  min(key[u], self.graph[u][v])
                    parent[v] = u
                    print(parent)

        self.printMST(parent)


g = Graph(6)
g.graph = [[0, 3, 9, 6, 0, 0],
           [3, 0, 2, 0, 7, 0],
           [9, 2, 0, 8, 5, 1],
           [6, 0, 8, 0, 0, 4],
           [0, 7, 5, 0, 0, 0],
           [0, 0, 1, 4, 0, 0]]


g.primMST();

# Contributed by Divyanshu Mehta