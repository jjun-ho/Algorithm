import random
from timeit import default_timer as timer

def heapify(A, k, n):  # index 0~n-1
    largest = k  # k, 부모 노드 index
    left = 2 * k + 1  # 자식 노드(왼쪽) index
    right = 2 * k + 2  # 자식 노드(오른쪽) index
    if left < n and A[left] > A[largest]:  # 자식 노드(왼쪽) 있다면 & 자식 노드(왼쪽) > 부모 노드
        largest = left  # 가장 큰수 = 왼쪽 자식 노드
    if right < n and A[right] > A[largest]:  # 자식 노드(오른쪽) 있다면 & 자식 노드(오른쪽) > 부모 노드
        largest = right  # 가장 큰수 = 오른쪽 자식 노드
    if largest != k:  # 가장 큰것이 부모 노드가 아니라면 = 자식 노드 중에서 부모 노드보다 더 큰 수가 있다면
        A[k], A[largest] = A[largest], A[k]  # 부모 노드 보다 큰 자식 노드와 부모 노드 맞바꿈
        heapify(A, largest, n)  # largest = 부모 노드(Root)

def heap_sort(A):
    n = len(A)
    for i in range(n//2 - 1, -1, -1):  # i: 자식이 있는 노드중 제일 마지막 index ~ 0
        heapify(A, i, n)
    for i in range(n-1, 0, -1):  # i:n-1~1 -> 힙 사이즈 하나씩 줄여준다 -> 아래서 맞바꾼 마지막 것(배열)을 제외한다
        A[0], A[i] = A[i], A[0]  # 처음과 마지막 (배열을) 맞바꾼다 (첫 번째 배열에 가장 큰수 정렬되어 있기 때문:내림차순)
        heapify(A, 0, i)  # 처음과 마지막 맞바꿨기 때문에 최대 힙 만족x -> Root에서 Heapify 다시 진행 -> 최대 힙 만족

def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.sample(range(10000), 100)
start = timer()
heap_sort(x)
print(timer() - start)
print(x)
print(test(x))

"""
* 힙 정렬(Heap Sort)
- 힙 구조의 특성을 이용한 정렬

* 힙의 형태
- 완전 이진 트리에 가까운 형태
-> Root 노드부터 Leaf 노드까지 빠짐없이 채워져 있는 트리
-> 마지막 레벨을 제외하고 모든 레벨을 완전히 채우고, 마지막 레벨은 왼쪽부터 채운다
1. 최대 힙(Max-Heap)
- 모든 부모 노드가 자식 노드보다 크거나 같은 완전 이진 트리
2. 최소 힙(Min-Heap)
- 모든 부모 노드가 자식 노드보다 작거나 같은 완전 이진 트리

* 힙 만들기(최대 힙) - Max Heapify
1. 자식이 있는 마지막 노드부터 시작
2. 자식이 더 크면 큰 자식과 맞 바꾸면서 내려간다
3. 처음과 마지막 (배열을) 맞바꾼다 (첫 번째 배열에 가장 큰수 정렬되어 있기 때문:내림차순)
4. 마지막 것을 제외한다
5. Root에서 시작해서 2~4 과정 반복한다 (3번 과정 때문에 Root만 최대 힙 성질 만족x)

* 힙 정렬의 장점 (완전 이진 트리)
1. 깊이가 최소
2. 배열로 구현 가능
- 부모 노드 안댁스 = (자식 노드 인덱스 - 1)/2 의 몫
- 자식 노드 안댁스(Left) = (부모 노드 안댁스)*2 + 1
- 자식 노드 안댁스(Right) = (부모 노드 안댁스)*2 + 2

* 노드의 높이
- 노드의 높이는 현재 노드에서 leaf 노드까지 내려갈 때 가장 단순하게 내려가는 가장 긴 경로에서 거쳐야 하는 간선의 
- 노드 수 = n -> 높이 = Θ(nlogn) (log의 밑 2):
Heap은 완전 이진 트리 구조를 가지기 때문에 각 레밸마다 노드의 수가 2배씩 증가하기 때문

* 힙 정렬의 성능 분석
- 깊이 logn (완전 이진 트리)
-> 1. 자식이 있는 노드중 제일 마지막부터 Heapify:
n = A.length, i: n//2 - 1 ~ 0 -> (1/2)*n 번 반복 -> ((1/2)*n)*logn -> 계수 무시 -> n*logn 
-> 2. 처음과 마지막 (배열을) 맞바꾸는 작업 - Heap Sort :
n = A.length, i: n = A.length-1 ~ 1 -> n*logn 
-> 1(Heapify) + 2(Heap Sort) = n*logn + n*logn = 2n*logn -> 계수 무시 -> n*logn 
-> T(n) = Θ(n*logn) 
"""