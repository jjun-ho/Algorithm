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
- 각 노드는 하나의 키 값을 가진다
- 각 노드의 키 값은 모두 달라야 한다
- 각 노드는 최대 두 개의 자식 노드를 갖는다
- 각 노드의 키 값은 왼쪽의 모든 노드의 키 값보다 크고 오른쪽의 모든 노드의 키 값보다 작다
"""