from math import sqrt
from utils import distance
from settings import *


# class Node:
#     def __init__(self, label, x, y):
#         self.label = label
#         self.x = x
#         self.y = y
#
#     def pos(self):
#         return self.x, self.y
#
#     # def __repr__(self):
#     #     return '{}({},{})'.format(self.label, self.x, self.y)
#
#
# class Edge:
#     def __init__(self, node1, node2):
#         self.nodes = (node1.label, node2.label)
#         self.length = sqrt((node1.x - node2.x) ** 2 + (node2.x - node2.y) ** 2)
#         self.pos = (node1.x, node1.y, node2.x, node2.y)
#
#     def __str__(self):
#         return "{}-{}".format(*self.nodes)
#
#     def to_tuple(self):
#         return self.nodes


class Path:
    """
    Path is a list of edges and nodes
    """

    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = []
        self.positions = POSITIONS
        self.length = 0
        for i in range(len(nodes) - 1):
            self.edges.append((nodes[i], nodes[i + 1]))
            self.length += distance(self.positions[nodes[i]], self.positions[nodes[i + 1]])

    @property
    def id(self):
        return ''.join(self.nodes)

    def __str__(self):
        return ''.join(self.nodes)

    def __repr__(self):
        return str(self) + ' LEN=' + str(round(self.length, 2))

    def swap(self, i, j):
        self.nodes[i], self.nodes[j] = self.nodes[j], self.nodes[i]

    def update_edges(self):
        self.length = 0
        self.edges = []
        for i in range(len(self.nodes) - 1):
            self.edges.append((self.nodes[i], self.nodes[i + 1]))
            self.length += distance(self.positions[self.nodes[i]], self.positions[self.nodes[i + 1]])
