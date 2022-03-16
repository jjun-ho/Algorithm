import random
from timeit import default_timer as timer

def bubble_sort(A):  # 버블 정렬 함수
    for last in range(len(A)-1, 0, -1):  # last: (n-1)~1
        sorted = True  # 종료 조건 추가
        for i in range(last):  # i: 0~(last-1 = n-2)
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                sorted = False # 맞바꾸는 일이 한번이라도 발생한 경우 = 정렬이 안되어있다
        if sorted:  #last = n-1일 때, i: 0~(last-1) -> 맞바꾸는 한번도 없다 = 이미 정렬 되어 있음 -> 더 이상 반복x
            break

def test(A):  # 정렬이 되어있는지 확인하는 함수
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

x = random.sample(range(10000), 100)
start = timer()
bubble_sort(x)
print(timer() - start)
print(x)
print(test(x))

"""
* 버블 정렬(Bubble Sort)
- 뒤에서 부터 앞으로 정렬을 해나가는 구조
- 맨 첫번째 값부터 시작해서 다음 값들과 차례로 비교하면서 앞의 값이 더 크면 뒤의 값과 자리를 바꾸면 된다
- 버블 정렬은 점점 큰 값들을 뒤에서 부터 앞으로 하나씩 쌓여 나가게 때문에 후반으로 갈수록 정렬 범위가 하나씩 줄어들게 된다

* 버블 정렬의 성능 분석
last = n-1, i = 0~n-2: n-1번
last = n-2, i = 0~n-3: n-2번
...
last = 1, i = 0~0: 1번
- 합계: (n-1) + (n-2) + ...+ 1 = n(n-1)/2 번
- 시간 복잡도 Θ(n^2)
- 최선의 경우(Best Case) = 이미 정렬되어 있는 경우 = 시간 복잡도 Θ(n)
"""