import random
from timeit import default_timer as timer

def insertion_sort(A):  # 삽입 정렬 함수
    for i in range(1, len(A)):  # i: 1~(n-1)
        loc = i - 1  # loc: (i-1)~0,
        new_item = A[i]  # A[i]: key 값
        while loc >= 0 and new_item < A[loc]:  # 최대 i번 반복(정렬된 숫자와 지금 key 값에 따라)
            A[loc+1] = A[loc]  # new_item < A[loc]이면 앞쪽에 삽입 해야하기 때문에, 뒤(오른쪽)로 민다
            loc -= 1  # new_item >= A[loc] or loc < 0 가 될 때까지, loc--
        A[loc+1] = new_item  # while 나오면서 이미 loc 값 -1 되어있기 때문에, 삽입 위치 loc+1

def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.sample(range(10000), 100)
start = timer()
insertion_sort(x)
print(timer() - start)
print(x)
print(test(x))

"""
* 삽입 정렬(Insertion Sort)
- 삽입을 이용한 정렬 알고리즘
- key 값과 정렬된 리스트가 주어졌을 때, key 값을 정렬된 리스트의 알맞은 위치에 삽입
- 삽입 정렬은 key 값을 하나씩 추가하면서 정렬한다
A[1,,,n]이 주어진 배열이라고 하면
1. A[2]을 정렬된 배열 A[1]에 집어넣는다
2. A[3]을 정렬된 배열 A[1,2]에 집어넣는다
...
n-1. A[n]을 정렬된 배열 A[1,2,,,n-1]에 집어넣는다

* 삽입 정렬의 성능 분석
i = 1, loc = 0~0: 1번
i = 2, loc = 1~0: 2번
...
i = n-1, loc = n-2~0: n-1번
- 합계: 1 + 2 + ... + (n-1) = n(n-1)/2 번
- 시간 복잡도 Θ(n^2)
- 최선의 경우(Best Case) = 이미 정렬되어 있는 경우(key 값 앞 항상 key 값보다 작다) -> while문 수행 안 함(비교 1번만) -> 시간 복잡도 Θ(n)
- 거의 정렬되어 있는 경우 Θ(n)에 가까움
- 최악의 경우 = 반대 순서로 정렬되어 있는 경우 -> key 값 앞에 정렬된 배열들은 항상 key 값보다 크다 -> 항상 key 값과 key 값 숫자 만큼 비교 
"""