import random
from timeit import default_timer as timer

def sequential_search(x, value):
    n = len(x)
    for i in range(n):
        if x[i] == value:
            return i
    return -1

x = random.sample(range(5000), 1000)
value = x[800]  # 찾을 값 (비교를 위해 인덱스를 고정)

start = timer()
index = sequential_search(x, value)
print(timer() - start)

print('value', value, 'found', index)  # 찾을 값의 인덱스가 800이므로 800 출력
print(True if index >= 0 and x[index] == value else False)  # 찾을 값과 찾은 값이 같으면 True / 아니면 False
"""
* 선형 탐색(순차 탐색)
- 처음부터 끝까지 순서대로 탐색
"""