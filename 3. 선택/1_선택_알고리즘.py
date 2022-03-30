import random
from timeit import default_timer as timer

def partition(A, p, r):  # 퀵 정렬의 Partition
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

def SELECT(A,p,r,i):  # p부터 r까지 범위, i번째 작은 원소 찾기
    if p == r:  # 데이터 하나
        return A[p]
    q = partition(A,p,r)  # q: 기준 값의 위치(인덱스)
    k= q - p + 1  # 기준 값이 k번째 작은 원소임
    if i < k:
        return SELECT(A,p,q-1,i)
    elif i == k:
        return A[q]
    else:
        return SELECT(A,q+1,r,i-k)  # 오른쪽에서 (i-k)번 째 원소 찾기

x = random.sample(range(10000), 100)
start = timer()
print(SELECT(x,0,99,50))  # 0~99 중, 50번 째 원소 찾기
print(timer() - start)
print(x)
"""
* 선택 알고리즘
- n개 중 i번째 작은 원소 찾기
- 한번 씩은 봐야 하므로 Ω(n)
- O(nlogn)인 정렬 알고리즘 사용  -> O(nlogn)
- Ω(n)과 O(nlogn) 사이일 것으로 추정

p: 시작 인덱스, q: 기준 인덱스
q-p개 / k=q-p+1 번째 / k+1번째 -> 오른쪽 구역 1번째
                   / k+m번째 -> 오른쪽 구약 m번째
                   / k+(i-k)번째 -> 오른쪽 구역 (i-k)번째

* 선택 알고리즘 시간 복잡도
- 𝑇(𝑛) ≤ 𝑚𝑎𝑥(𝑇(𝑘−1), 𝑇(𝑛−𝑘)) + Θ(𝑛)
                 k 기준       Partition
- 평균
-> 𝑇(𝑛) ≤ (1/n) * (k=1~n)∑𝑚𝑎𝑥(𝑇(𝑘−1), 𝑇(𝑛−𝑘)) +Θ(𝑛) 
        ≤ (2/n) * (k=([n/2]~(n-1))∑𝑇(𝑘) + Θ(𝑛)
-> k < n인 모든 k에 대해 T(k) <= ck 라고 가정
-> 𝑇(𝑛) ≤ (2/n) * (k=([n/2]~(n-1))∑ck + Θ(𝑛)
       ≤ (2/n) * {(k=1~(n-1))∑ck - (k=(1~([n/2]-1))∑ck} + Θ(𝑛)
       ≤ (2c/n) * {n(n-1)/2 - (n/2-1)(n/2-2)/2} + Θ(𝑛)
       ≤ cn - c(n/4 - 1/2 + 2/n) + Θ(𝑛) ≤ cn - 0 (: 충분히 큰 c에 대해 c >= Θ(𝑛)/(n/4 - 1/2 + 2/n))
-> T(n) = O(n)

- 평균
-> 한번 씩은 봐야 하므로 T(n) = Ω(n)
-> T(n) = O(n)
- T(n) = Θ(𝑛)

- Worst(=퀵정렬 Worst: 퀵정렬 Partition 할 때 한 개씩만 떨어져 나갈 때)
-> T(n) = T(n-1) + Θ(𝑛)
- T(n) = Θ(𝑛^2)

* 분할 비율
ex) 1:9로 계속 분할되고 9그룹에 계속 해당
T(n) = T(9n/10) + Θ(𝑛)
𝑇(𝑘) ≤ 𝑐𝑘, ∀𝑘 < 𝑛 라고 가정
𝑇(𝑛) =𝑇(9𝑛/10) + Θ(𝑛) ≤ (9c/10)*n + Θ(𝑛) = cn − (1/n)cn + Θ(n)
충분히 큰 𝑐 ≥ 10*Θ(𝑛) / n 에 대해 
𝑇(𝑛) ≤ cn -> 𝑇(𝑛) = 𝑂(𝑛)
𝑇(𝑛) = Ω(𝑛)
=> 𝑇(𝑛) = Θ(𝑛)

* 최악에도 선형 시간 선택 알고리즘
1. 원소 5개인 그룹(마지막은 5개 이하)으로 나눈다
2. 각 그룹의 중간 값을 찾는다
3. 각 중간 값들의 중간 값 M을 찾는다
4. 최악의 경우는 O(M보다 큰지 작은지 모르는 것)들이 모두 한쪽에 쏠리는 경우

- 모두 M의 왼쪽에 쏠렸다면
-> M보다 큰 것 개수 = 최소 3n/10 - 3 개 -> M포함 최소 3n/10 - 2 개
-> 나머지는 n - (3n/10 - 2) = 7n/10 + 2개
-> 최악의 경우 7n/10 + 2 : 3n/10 - 2 으로 분할  -> n 무수히 크면 7:3
- 최악의 경우 시간 복잡도
𝑇(𝑛) ≤ 𝑇([n/5]) + 𝑇(7𝑛/10 + 2) + Θ(𝑛) 
     ≤ 𝑇(𝑛/5+1) + 𝑇(7𝑛/10 + 2) + Θ(𝑛) 
 𝑇(𝑘) ≤ 𝑐𝑘, (∀𝑘, n/5 ≤ 𝑘 < 𝑛) 라고 가정
𝑇(𝑛) ≤ 𝑇(𝑛/5+1) + 𝑇(7𝑛/10 + 2) + Θ(𝑛)
     ≤ 𝑐(n/5 + 1 + 7n/10 +2) + Θ(𝑛) = 𝑐(9n/10 + 3) + Θ(𝑛)
 충분히 큰 𝑐 ≥ 10 * Θ(𝑛) / (n-30) 에 대해 
𝑇(𝑛) ≤ 𝑐𝑛 -> 𝑇(𝑛) = 𝑂(𝑛) 
𝑇(𝑛) = Ω(𝑛)
=>  T(n) = Θ(𝑛) : i번째 원소 찾는 것 < 정렬 T(n) = Θ(nlogn)
"""