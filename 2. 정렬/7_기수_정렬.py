import random
from timeit import default_timer as timer

def rsort(A, m):
    buckets = [[] for _ in range(10)]  # 빈 리스트 10개로 구성된 리스트, 자릿수로 올수있는 값 0~9
    for v in A:
        index = v // (10 ** m)
        index %= 10
        buckets[index].append(v)  # 리스트에 값 추가
    res = []
    for bucket in buckets:
        res.extend(bucket)   # 리스트 res에 리스트 bucket의 모든 값 추가
    return res

def radix_sort(A, k):  # k: 최대 자리수
    for i in range(0, k):  # i:0 ~ k-1, i번째 자릿수 기준 정렬
        A = rsort(A, i)
    return A

def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.sample(range(10000), 100)  # 0~9999 범위에서 중복없이 100개
start = timer()
x = radix_sort(x, 4)
print(timer() - start)
print(x)
print(test(x))
"""
* 기수 정렬(Radix Sort)
- 입력이 모두 k 자릿수 이하의 자연수인 경우
- 자릿수 별로 안정성을 유지하며 정렬: Stable Sort (값이 같은 원소는 정렬 전후 순서가 바뀌지 않음)

* 기수 정렬의 성능 분석
- O(n)을 k(자릿수) 반복 -> O(n)

cf)
* 기수 정렬의 수행 시간
- Θ(d(n+k))
-> d 자리 수 숫자 n 개가 주어졌을 때, 각 자리 수에서 최대 k값을 가질 수 있다고 가정
-> d가 상수이고 k=O(n)이므로 기수 정렬은 선형시가에 수행 -> Θ(n)
"""