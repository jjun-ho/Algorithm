import random
from timeit import default_timer as timer

class Node(object):
    def __init__(self, key):  # 생성자
        self.key = key
        self.left = None
        self.right = None

def insert(node, key):  # BST: 이진 검색 트리
    if node is None: node = Node(key)  # 노드 없으면
    elif key < node.key: node.left = insert(node.left, key)  # 현재 노드 왼쪽에 추가
    else: node.right = insert(node.right, key) # 현재 노드 오른쪽에 추가
    return node

def search(node, key):
    if node is None or node.key == key: return node
    if key < node.key: return search(node.left, key)
    return search(node.right, key)

"""
# 노드 삭제
class Node(object):
    def __init__(self, key, parent):  # 생성자
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent

def DELETE_NODE(r):  # r: 삭제할 노드
    if r.left is None and r.right is None:  # r의 자식 0개 -> 그냥 삭제
        return None
    elif r.left is not None and r.right is None:  # r의 자식(왼쪽) 1개 -> r부터 시작하는 서브 트리에서 r을 삭제한 후 서브 트리의 루트를 반환
        return r.left
    elif r.right is not None and r.left is None:  # r의 자식(오른쪽) 1개 -> r부터 시작하는 서브 트리에서 r을 삭제한 후 서브 트리의 루트를 반환
        return r.right
    else:  # r의 자식 2개 -> r이 삭제된 후 r 자리를 차지하게 되는 노드를 반환
        s = r.right
        while s.left is not None:  # 왼쪽 자식 있으면(없을 때까지)
            sparent = s
            s = s.left
        r.key = s.key  # r에 내용 복사
        if s == r.right:  # 특수한 경우(위 while문 수행 안함)
            r.right = s.right
        else:  # 대분분의 경우: s의 왼쪽 자식은 없음(크기가 r 바로 다음인 노드이기 때문 = r의 오른쪽 자식에서 제일 작은 노드이기 때문 )
            sparent.left = s.right  # s는 sparent의 왼쪽 자식
        return r

def DELETE(node):
    if node == root:
        root = DELETE_NODE(node)
    elif node == node.parent.left:  # 부모 노드의 왼쪽 노드 라면
        node.parent.left = DELETE_NODE(node)
    else:  # 부모 노드의 오른쪽 노드 라면
        node.parent.right = DELETE_NODE(node)
"""

x = random.sample(range(5000), 1000)  # 무작위로 1000개를 뽑아 데이터를 만든다
value = x[800]  # 찾을 값(비교를 위해 인덱스를 고정)

root = None  # 초기 root = None
for i in x:  # 1000개 데이터 추가
    root = insert(root, i)

start = timer()
found = search(root, value)
print(timer() - start)

if found is not None:
    print('value', value, 'found', found.key)
    print(True if found.key == value else False)  # 찾을 값과 찾은 값이 같으면 True, 아니면 False

"""
* 이진 검색 트리(Binary Search Tree)
- 각 노드는 하나의 키 값을 가진다
- 각 노드의 키 값은 모두 달라야 한다
- 각 노드는 최대 두 개의 자식 노드를 갖는다
- 각 노드의 키 값은 왼쪽의 모든 노드의 키 값보다 크고 오른쪽의 모든 노드의 키 값보다 작다

* 이진 검색 트리의 단점
- 데이터 입력 순서에 따라 성능이 달라진다.
ex) 같은 data
-> 무작위 순서대로 입력(왼쪽 노드/ 오른쪽 노드 거의 반반): 왼쪽 노드 or 오른쪽 노드 이동하면서 대입 
= 높이 만큼 비교 -> Θ(log2n)
-> 작은 순서대로 입력: 계속 오른쪽으로 대입 
= data 개수만큼 비교 -> Θ(n)
"""