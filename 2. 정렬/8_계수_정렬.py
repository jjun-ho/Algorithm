import random
from timeit import default_timer as timer

def counting_sort(A, k):
    B = [0] * len(A)
    C = [0] * (k+1)  # 몇 개인지 저장하는 카운트 list
    for v in A:
        C[v] += 1  # 카운트
    for i in range(1, k+1):
        C[i] += C[i-1]  # 누적 카운트
    for i in range(len(A)-1, -1, -1):  # (n-1)~0
        v = A[i]
        C[v] -= 1
        B[C[v]] = v
    return B

def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.choices(range(50), k=100)  # 0~49 범위에서 중복 허용하여 100개
start = timer()
print(x)
x = counting_sort(x, 49)
print(timer() - start)
print(x)
print(test(x))
"""
* 계수 정렬(Counting Sort)
- 계수를 이용하여 정렬: 입력 받은 배열에 있는 숫자의 범위를 확인하고 몇 개가 있는지를 세어보고 정렬하는 알고리즘
- 입력 값이 모두 k(최대값) 이하인 경우 -> 입력된 숫자의 범위(k)가 작을 수록 유리
- k <= O(n)인 경우에만 의미가 있음
- 같은 값이 몇 개인지 세어서 워치 결정 -> 입력이 많이 중복될수록 유리
- 입력 배열의 순서가 정렬 후에도 유지된다: stable

* 계수 정렬의 성능 분석
- k <= O(n) -> O(n)
- Θ(k) + Θ(n) + Θ(k) + Θ(n)
-> O(n) + O(n) + O(n) + O(n) = O(n)

cf)
* 계수 정렬의 수행 시간
-> 전체 수행시간은 Θ(k+n)
- k는 입력되는 정수의 범위이다.
- 만약 k=O(n)라면, 수행시간은 Θ(n)이 된다.
"""
