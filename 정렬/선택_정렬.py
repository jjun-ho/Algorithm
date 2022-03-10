import random
from timeit import default_timer as timer  # 시간 측정을 위해 import

def selection_sort(x): #선택 정렬 함수
    for last in range(len(x)-1, 0, -1):  # last, last ~ 1 까지 하나씩 감소
        largest = 0 # 가장 큰수의 index
        for i in range(1, last+1):  # i, 1~last 까지 하나씩 증가
            if x[i] > x[largest]:
                largest = i
            x[largest], x[last] = x[last], x[largest]  # 맞바꾸기

def test(x):  #정렬이 되어있는지 확인하는 함수
    for i in range(1,len(x)):
        if x[i-1] > x[i]:
            return False
    return True

data = random.sample(range(10000), 100)  # 0~9999까지 중, 100개의 random data 만들기
start = timer()
selection_sort(data)
print(timer() - start)  # 현재시간 - 시작시간 = 걸린시간
print(data)
print(test(data))

"""
* 선택 정렬(Selection Sort)
1. index 0번부터 마지막(last)까지 하나씩 비교 하면서 가장 큰수의 index를 largest 변수에 저장한다.
2. 가장 큰수와 가장 마지막 index(last)에 있는 수를 맞바꾼다.
3. last 값을 하나 줄인다.
4. 1~3 과정을 반복한다.
"""