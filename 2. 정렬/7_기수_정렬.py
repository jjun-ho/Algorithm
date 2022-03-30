import random
from timeit import default_timer as timer

def rsort(A, m):
    buckets =  [[] for _ in range(10)]
    for v in A:
        index = v // (10 ** m)
        index %= 10
        buckets[index].append(v)
    res = []
    for bucket in buckets:
        res.extend(bucket)
    return res

def radix_sort(A, k):
    for i in range(0, k):
        A = rsort(A, i)
    return A

def test(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.sample(range(10000), 100) start = timer()
x = radix_sort(x, 4)
print(timer() - start)
print(x)
print(test(x))
"""
* 기수 정렬(Radix Sort)
- 입력이 모두 k 자릿수 이하의 자연수인 경우
- 자릿수 별로 안정성을 유지하며 정렬: Stable Sort (값이 같은 원소는 정렬 전후 순서가 바뀌지 않음)
"""