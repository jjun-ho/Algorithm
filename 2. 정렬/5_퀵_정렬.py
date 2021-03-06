"""
# < 퀵 정렬 코드 1 (중간에 있는 것을 피벗으로 사용) >
import random
from timeit import default_timer as timer

def quick_sort(A):
    if len(A) <= 1:
        return A
    x = A[len(A) // 2] # 피벗
    less = []
    more = []
    equal = []  # quick_sort가 호출될 때마다 빈 리스트 새로 만든다 -> 낭비
    for a in A:
            if a < x:
                less.append(a)
            elif a > x:
                more.append(a)
            else:
                equal.append(a)
    return quick_sort(less) + equal + quick_sort(more)

def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.sample(range(10000), 100)
start = timer()
x = quick_sort(x)
print(timer() - start)
print(x)
print(test(x))
"""

"""
# < 퀵 정렬 코드 2 (제일 왼쪽에 있는 것을 피벗으로 사용) >
import random
from timeit import default_timer as timer

def partition(A, p, r):
    x = A[p]
    left = p + 1  # i index
    right = r  # j index
    while True:
        while left <= right and A[left] <= x:
            left += 1
        while left <= right and x <= A[right]:
            right -= 1
        if right < left:  # i, j 교차 되었을 때
            break
        else: # i, j 교차 되지 않았을 때
            A[left], A[right] = A[right], A[left]
    A[p], A[right] = A[right], A[p]
    return right

def qsort(A, p, r):
    if p < r:  # p = r -> 낱개로 다 나누어졌을 때
        q = partition(A, p, r)
        qsort(A, p, q - 1)
        qsort(A, q + 1, r)


def quick_sort(A):
    qsort(A, 0, len(A)-1)

def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.sample(range(10000), 100)
start = timer()
quick_sort(x)
print(timer() - start)
print(x)
print(test(x))
"""

# < 퀵 정렬 코드 3 (제일 오른쪽에 있는 것을 피벗으로 사용) >
import random
from timeit import default_timer as timer

def partition(A, p, r):
    x = A[r]  # 피벗(제일 오른쪽에 있는 것)
    i = p   # i index
    for j in range(p, r):  # j: p~r-1
        if A[j] <= x:  # A[j] < 피벗
            A[i], A[j] = A[j], A[i]  # A[i], A[j] exchange
            i += 1  # i 이동
    A[i], A[r] = A[r], A[i]  # 끝났으면 A[i], A[r] exchange
    return i  # 피벗 index

def qsort(A, p, r):
    if p < r:  # p = r -> 낱개로 다 나누어졌을 때
        q = partition(A, p, r)
        qsort(A, p, q - 1)  # 낱개로 다 나누어질 때까지
        qsort(A, q + 1, r)

def quick_sort(A):
    qsort(A, 0, len(A)-1)

def test(A):  # 오름차순으로 정렬되어 있는지 확인하는 함수
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.sample(range(10000), 100)
start = timer()
quick_sort(x)
print(timer() - start)
print(x)
print(test(x))

"""
* 퀵 정렬(Quick Sort)
- Divide-and-Conquer paradigm을 사용
- Partitioning 
-> Pivot element(기준) 보다 작은 것은 왼쪽 / 큰 것은 오른쪽 
-> 모두 낱장으로 나누어 질 때까지 반복
-> 작은 값 앞으로 / 큰 값 뒤쪽으로
- 피벗 선정 -> 성능의 큰 영향

* 피벗 선정
- 피벗을 기준으로 그룹을 계속 나누기 때문에 피벗이 한쪽에 쏠려 있는 것보다 가운데 있는 것이 좋다 -> 빠른 속도로 그룹이 낱개로 쪼개짐
1. 무작위 퀵 정렬
2. 중간 값(값의 중간)을 피벗으로 사용: 정렬을 요구 -> x
3. 중간에 있는 것을 피벗으로 사용
4. 첫 번째 것을 피벗으로 사용: 별로 좋지 않은 방법(이미 정렬된 데이터에 대해 최악의 성능)
5. 첫 번째, 마지막, 중앙에 있는 3개의 값에 대해 중간 값을 구하여 피벗으로 사용

* 첫 번째 것을 피벗으로 사용
- 이미 정렬된 데이터: 최악의 경우 -> 첫 번째 것만 떨어져 나옴 -> data 개수 만큼 반복 
1. A[i] > A[p]일 때까지 이동(->), i는 j+1까지만 이동 가능
2. A[j] < A[p]일 때까지 이동(<-), j는 i-1까지만 이동 가능
3-1. i와 j가 서로 지나치지 않았으면 A[i], A[j] 맞교환
3-2. i와 j가 서로 지나쳤으면 A[j], A[p] 맞교환 후, 피벗의 위치를 j로 변경

* 마지막 것을 피벗으로 사용
- 이미 정렬된 데이터: 최악의 경우 -> 젤 오른쪽(마지막) 것만 하나씩 떨어져 나옴 -> data 개수 만큼 실행
1. j를 처음부터 r-1까지 이동(j++)
2-1. A[j] <= A[r]이면 A[i], A[j] 맞교환 후, i 이동(i++) : A[r]보다 큰 것은 오른쪽으로 이동
2-2. A[j] > A[r]이면 j 다음으로 이동(j++)
3. 끝났으면 A[i], A[r] 맞교환 (A[i] 는 피벗 왼쪽에 피벗보다 큰 수 중 가장 작은 수)
4. 피벗 기준으로 나누어서 반복

* 퀵 정렬의 성능 분석
피벗과 나머지 n-1비교: c1*n + c2
- 최악의 경우(이미 오름차순으로 정렬되어 있는 경우): 
T(n) = T(n-1) + (c1*n + c2) 
-> T(n) = Θ(n^2)
- 최상의 경우:
T(n) = 2*T(n/2) + (c1*n + c2) 
-> T(n) = Θ(𝑛log𝑛)
- 평균적인 경우: 
𝑇(𝑛) = 𝑇(𝑖−1) + 𝑇(𝑛−𝑖) + (𝑐1*𝑛+𝑐2)
𝑇(𝑛) =(1/n) * (i:1~n)∑(T(i-1) + T(n-i)) + (𝑐1*𝑛+𝑐2)  # i: 1~n -> T(i-1): 0~n-1, T(n-i): 0~n-1
𝑇(𝑛) =(2/n) * (k:0~n-1)∑(T(k)) + (𝑐1*𝑛+𝑐2)
-> 𝑇(𝑛) =  Θ(𝑛log𝑛)

cf)
* 퀵 정렬의 수행시간
- Partition에 걸리는 시간: 피벗과 나머지 n-1 비교 -> 피벗보다 작으면 왼쪽/ 크면 오른쪽 -> n-1번: Θ(n) 
- Partition의 횟수
1. Balanced Partitioning
-> 각 하위 문제의 크기가 기존 문제의 크기의 절반 정도인 (n/2) 과 (n/2 - 1)가 되도록 나누어지는 경우
-> T(n) <= 2T(n/2) + Θ(n) = 0(nlog𝑛) 
2. Unbalanced Partitioning
-> T(n) = T(n-1) + Θ(n) = Θ(n^2) 
"""