class Node(object):
    def __init__(self, key, parent, color):  # 생성자
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color

def right_rotate(X):  # 오른쪽 회전
    Y = X.left
    X.left = Y.right
    if Y.right != None:
        Y.right.parent = X
    Y.parent = X.parent
    if X.parent == None:
        root = Y
    elif X == X.parent.right:
        X.parent.right = Y
    else:
        X.parent.left = Y
    Y.right = X
    X.parent = Y

def left_rotate(X): # 왼쪽 회전
    Y = X.right
    X.right = Y.left
    if Y.left != None:
        Y.left.parent = X
    Y.parent = X.parent
    if X.parent == None:
        root = Y
    elif X == X.parent.left:
        X.parent.left = Y
    else
        X.parent.right = Y
    Y.left = X
    X.parent = Y

def BST_insert(node, key):  # 이진 검색 트리 insert
    if node is None: node = Node(key)  # 노드 없으면
    elif key < node.key: node.left = BST_insert(node.left, key)  # 현재 노드 왼쪽에 추가
    else: node.right = BST_insert(node.right, key) # 현재 노드 오른쪽에 추가
    return node

# 삽입: 새로운 키를 트리에 추가
def RB_insert(N):
    BST_insert(N)  # 이진 검색 트리 똑같이 노드 삽입
    while N.parent.color == RED: # 균형 맞춰줌
        if N.parent == N.parent.parent.right: # P가 오른쪽 자식
            U = N.parent.parent.left
            if U.color == RED:  # Case 3-1
                U.color == BLACK
                N.parent.color = BLACK
                N.parent.parent.color = RED
                N = N.parent.parent
            elif N == N.parent.left:  # Case 3-2-2
                N = N.parent
                right_rotate(N)
            N.parent.color = BLACK  # Case 3-2-1
            N.parent.parent.color = RED
            left_rotate(N.parent.parent)
        else:  # P가 왼쪽 자식
            U = N.parent.parent.right
            if U.color == RED:
                U.color == BLACK
                N.parent.color = BLACK
                N.parent.parent.color = RED
                N = N.parent.parent
            elif N == N.parent.right:  # p가 왼쪽 자식, N이 오른쪽 자식
                N = N.parent
                left_rotate(N)
            N.parent.color = BLACK  # P가 왼쪽 자식, N이 왼쪽 자식
            N.parent.parent.color = RED
            right_rotate(N.parent.parent)
    root.color = BLACK

# 검색: 찾는 키를 가지고 있는 노드를 반환
def search(root, data):
    if root is None or root.data == data:
        return root
    elif root.data >= data:
        return search(root.left, data)
    elif root.data < data:
        return search(root.right, data)

"""
* 레드 블랙 트리(Red Black Tree)
- AVL 트리처럼 균형을 맞추지만 완전히 균형을 맞추지 않음
-> 대략~ 균형 잡힌 이진 검색 트리

* 레드 블랙 트리 조건
- NIL(None)을 채우고 리프로 처리(일반적인 리프 노드와 다름)
- 루트는 블랙
- 모든 리프는 블랙
- 레드의 자식은 블랙(레드가 연속 2개일 수 없다)
-> 최소 높이는 모두 블랙인 경우
-> 최대 높이는 레드-블랙 교대로인 경우
- 루트에서 리프까지 모든 경로는 같은 개수의 블랙
-> 최악의 경우(최대 높이)에도 최소 높이의 2배 이하

* 레드 블랙 트리 시간 복잡도
- 최악의 경우에도 최소 높이의 2배 이하
- 최소 높이가 logn
->O(logn)
"""