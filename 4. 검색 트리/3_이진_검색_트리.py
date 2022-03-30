import random
from timeit import default_timer as timer

class Node(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(node, key):
    if node is None: node = Node(key)
    elif key < node.key: node.left = insert(node.left, key)
    else: node.right = insert(node.right, key)
    return node

"""
* 이진 검색 트리(Binary Search Tree)

"""