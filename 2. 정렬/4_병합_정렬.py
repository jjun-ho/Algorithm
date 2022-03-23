"""
# < 병합 정렬 코드 1 >
import random
from timeit import default_timer as timer

def merge_sort(A, p, r):  # 처음 p = 0, r = n-1
    if p < r:
        q = (p+r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    i, j, t = p, q+1, 0
    tmp = A[:]
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
        else:
            tmp[t] = A[j]
            j += 1
        t += 1
    while i <= q:
        tmp[t] = A[i]
        i += 1
        t += 1
    while j <= r:
        tmp[t] = A[j]
        j += 1
        t += 1
    i, t = p, 0
    while i <= r:
        A[i] = tmp[t]
        i += 1
        t += 1
        
def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True
x = random.sample(range(10000), 100)
start = timer()
merge_sort(x,0,len(x)-1)  # **
print(timer() - start)
print(x)
print(test(x))        
"""
# < 병합 정렬 코드 2 >
import random
from timeit import default_timer as timer

def merge_sort(x):
    if len(x) > 1:  # 나누어 질수 있다면(낱개로)
        mid = len(x) // 2   # mid = q
        lx, rx = x[:mid], x[mid:]  # [:mid]: 처음 ~ (mid-1), [mid:]: mid ~ 끝 리스트를 두 개의 리스트로 쪼갬
        merge_sort(lx)
        merge_sort(rx)
        li, ri, i = 0, 0, 0  # 쪼개진 각각의 리스트의 index는 0부터 시작
        while li < len(lx) and ri < len(rx):
            if lx[li] < rx[ri]:
                x[i] = lx[li]
                li += 1
            else:
                x[i] = rx[ri]
                ri += 1
            i += 1
        x[i:] = lx[li:] if li != len(lx) else rx[ri:]  # 비교 안된 남은 리스트 집어넣기
      # i ~ 끝 / li ~ 끝 /if 끝까지 안갔다(왼쪽 리스트가 남았다) / else 오른쪽 리스트가 남았다 (x[i:]=rx[ri:])

def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.sample(range(10000), 100)
start = timer()
merge_sort(x)  # **
print(timer() - start)
print(x)
print(test(x))

"""
* 병합 정렬(Merge Sort)
- 합병을 이용한 정렬 알고리즘
- 두 개의 정렬된 배열이 주어졌을 때, 정령된 하나의 배열로 합병
cf)
- A divide-conquer approach
-> 크기가 커서 풀기 어려운 하나의 문제를 크기가 작아서 풀기 쉬운 여러 개의 문제로 바꾸어서 푸는 방법
1. Divide: n keys를 두 개의 n/2 keys로 나눈다 (n -> n/2 -> ... -> 1) : Θ(1)
2. Conquer: 합병 정렬을 사용하여 두 개의 배열을 정렬한다 : 2𝑇(𝑛/2)
3. Combine: 두 개의 정렬된 배열을 하나로 합치는 과정 :  Θ(n)
T(n) = Θ(1)            (if n=1)  = c
     = 2𝑇(𝑛/2) + Θ(n)  (if n>1)  = 2𝑇(𝑛/2) + cn
     
* 병합 정렬의 성능 분석
𝑇(𝑛) = 2𝑇(𝑛/2) + 𝑐1n + 𝑐2
𝑎=2, 𝑏=2, h(𝑛) = 𝑛log22 = 𝑛,𝑓(𝑛) = 𝑐1𝑛 + 𝑐2
f(n)/h(n) = (c1n + c2)/n = c1 + c2/n  = Θ(1) (c1 <= c1 + c2/n <= c1 + c2 이므로)
마스터 정리 유형 (3)에 해당
𝑇(𝑛) = Θ(h(𝑛)log𝑛) = Θ(𝑛log𝑛)

cf)
* 합병 정렬의 수행시간
- 두 개의 정렬된 배열의 길이를 n1, n2 라고 하면 수행시간 Θ(n1 + n2)
- 주요 함수: compare 와 move
-> move 횟수: n1 + n2
-> compare 횟수 <= move 횟수
-> compare 횟수 + move 횟수 <= 2(n1 + n2)
-> Θ(n1 + n2 )
"""