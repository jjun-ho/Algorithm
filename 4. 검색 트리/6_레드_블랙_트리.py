class Node(object):
    RED = True
    BLACK = False
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
    else:
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

"""
cf) 레드 블랙 트리 전체

class Node:
    RED = True
    BLACK = False
    def __init__(self, value, color=RED):
        self.color = color
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.value) + ':' + str('R' if self.color else 'B')

    def verbose(self):
        return '{} (parent:{} left:{} right:{})'.format(self, self.parent, self.left, self.right)

class RedBlackTree:
    def __init__(self):
        self.root = None
    def max_depth(self, root=None):
        if root is None:
            return 0
        else:
            return max(self.max_depth(root.left), self.max_depth(root.right)) + 1

    def depth(self, node):
        if node is None:
            return 0
        node_ = node
        depth = 0
        while node_ != self.root:
            node_ = node_.parent
            depth += 1
        return depth

    def min(self, current=None):
        if not current:
            current = self.root
        while current.left is not None:
            current = current.left
        return current

    def max(self, current=None):
        if not current:
            current = self.root
        while current.right is not None:
            current = current.right
        return current

    def search(self, value):
        return self.__search(self.root, value)

    def __search(self, node, value):
        while node is not None and value != node.value:
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return node

    def successor(self, value):
        current = self.search(value)
        if current is None:
            raise Exception(('a Node with value ({})'' does not exist').format(value))
        return self.__successor(current)

    def __successor(self, current):
        if current.right is not None:
            return self.min(current.right)
        while (current.parent is not None and current.parent.right is current):
            current = current.parent
        return current.parent

    def insert(self, key):
        node = Node(key)
        x = self.root
        y = None
        while x is not None:
            y = x
            if key < x.value:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y is None:
            self.root = node
        elif key < y.value:
            y.left = node
        else:
            y.right = node
        node.left = None
        node.right = None
        node.color = Node.RED
        self.__insert_fixup(node)

    def __insert_fixup(self, x):
        while x != self.root and x.parent.color == Node.RED:
            if x.parent == x.parent.parent.left:
                y = x.parent.parent.right
                if y is not None and y.color == Node.RED:
                    x.parent.color = Node.BLACK
                    y.color = Node.BLACK
                    x.parent.parent.color = Node.RED
                    x = x.parent.parent
                else:
                    if x == x.parent.right:
                        x = x.parent
                        self.__left_rotate(x)
                    x.parent.color = Node.BLACK
                    x.parent.parent.color = Node.RED
                    self.__right_rotate(x.parent.parent)
            else:
                y = x.parent.parent.left
                if y is not None and y.color == Node.RED:
                    x.parent.color = Node.BLACK
                    y.color = Node.BLACK
                    x.parent.parent.color = Node.RED
                    x = x.parent.parent
                else:
                    if x == x.parent.left:
                        x = x.parent
                        self.__right_rotate(x)
                    x.parent.color = Node.BLACK
                    x.parent.parent.color = Node.RED
                    self.__left_rotate(x.parent.parent)
        self.root.color = Node.BLACK

    def __left_rotate(self, x):
        if not x.right:
            raise Exception("a right branch of Node is None")
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        else:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        y.left = x
        x.parent = y

    def __right_rotate(self, x):
        if not x.left:
            raise Exception("a right branch of Node is None")
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        else:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        y.right = x
        x.parent = y

    def transplant(self, node, newnode):
        if node.parent is None:
            self.root = newnode
        elif node == node.parent.left:
            node.parent.left = newnode
        else:
            node.parent.right = newnode
        if newnode is not None:
            newnode.parent = node.parent

if __name__ in "__main__":
    tree = RedBlackTree()
    for i in [100,3,4,22,54,35,14,56,20]:
        print('insert {} to tree'.format(i))
        tree.insert(i)
    print(tree.search(20))
"""