import random
from timeit import default_timer as timer

def binary_search(x, v):
    start = 0
    end = len(x) - 1
    while start <= end:
        mid = (start + end) // 2
        if x[mid] == v: return mid
        elif x[mid] < v: start = mid + 1
        else: end = mid - 1
    return -1

x = random.sample(range(5000), 1000)
x.sort()
value = x[800]

start = timer()
index = binary_search(x, value)
print(timer() - start)

print('value', value, 'found', index)
print(True if index >= 0 and x[index] == value else False)
"""
* 이진 탐색
- 임의의 데이터들 -> 순서대로 정렬한 후 이진 탐색
- 데이터를 입력할 때부터 정렬 -> 이진 탐색(검색) 트리

1. 중간 = (시작 + 끝)/2 의 몫
2-1. 찾을 값 > 중간: 시작 = 중간 + 1
2-2. 찾을 값 < 중간: 끝 = 중간 -1
2-3. 찾을 값 = 중간: 탐색 종료
"""