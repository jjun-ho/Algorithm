import random
from timeit import default_timer as timer  # 시간 측정을 위해 import

def selection_sort(x): # 선택 정렬 함수
    for last in range(len(x)-1, 0, -1):  # last, last(n-1)~1 까지 하나씩 감소: ~0 말고 ~1 까지 반복함으로서 마지막 비교 계산 안해도됨.
        largest = 0  # 가장 큰수의 index
        for i in range(1, last+1):  # i, 1~last 까지 하나씩 증가
            if x[i] > x[largest]:  # 비교
                largest = i
            x[largest], x[last] = x[last], x[largest]  # 맞바꾸기

def test(x):  # 정렬이 되어있는지 확인하는 함수
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
* 정렬 문제의 정의
- 입력(Input): n개의 숫자들의 배열 <a1, a2, ... , an>
- 출력(Output): 입력된 숫자의 배열이 a'1 <= a'2 <= ... <= a'n 조건을 만족하도록 다시 나열된 결과 <a'1, a'2, ..., a'n>
- 오름차순(Increasing Order) / 내림차순(Decreasing Order)

* 선택 정렬(Selection Sort)
- 선택하여 정렬하는 알고리즘: 최소값 선택 정렬 / 최대값 선택 정렬
1. 정렬되지 않은 숫자 중에 index 0번부터 마지막(last)까지 하나씩 비교 하면서 가장 큰수의 index를 largest 변수에 저장한다.
2. 가장 큰수와 가장 마지막 index(last)에 있는 수를 맞바꾼다.
3. last 값을 하나 줄인다.
4. 1~3 과정을 반복한다.

* 선택 정렬의 정확성 증명
- 수학적 귀납법을 이용
- i번째 선택한 숫자가 i번째로 큰(작은) 숫자인지를 증명

* 선택 정렬의 성능분석
last = n-1, i = 1~n-1: n-1번
last = n-2, i = 1~n-2: n-2번
...
last = 1, i = 1~n-1: 1번
합계: (n-1) + (n-2) + ...+ 1 = n(n-1)/2 번
시간 복잡도 Θ(n^2)
cf) 항상 모든 수를 전부 비교하기 때문에 최선/최악의 경우는 없다
"""