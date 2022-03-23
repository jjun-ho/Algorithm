< 정렬 문제의 정의 >
- 입력(Input): n개의 숫자들의 배열 <a1, a2, ... , an>
- 출력(Output): 입력된 숫자의 배열이 a'1 <= a'2 <= ... <= a'n 조건을 만족하도록 다시 나열된 결과 <a'1, a'2, ..., a'n>
- 오름차순(Increasing Order) / 내림차순(Decreasing Order)
---
< 시간 복잡도 비교(선택 / 버블 / 삽입)>

        Best    Worst   Average
선택 정렬 Θ(n^2)  Θ(n^2)   Θ(n^2)

버블 정렬 Θ(n)    Θ(n^2)   Θ(n^2)

삽입 정렬 Θ(n)    Θ(n^2)   Θ(n^2)

합병 정렬 Θ(nlog𝑛) Θ(nlog𝑛) Θ(nlog𝑛) 

퀵 정렬  Θ(nlog𝑛) Θ(n^2)   Θ(nlog𝑛) 

힙 정렬  Θ(nlog𝑛) Θ(nlog𝑛) Θ(nlog𝑛)

cd) 퀵 정렬보다 합병 정렬이 Worst 경우 더 빠르지만, memory 좀더 사용

---
< 비교 정렬 시간의 하한 >

비교 정렬 
- 원소끼리 비교하는 것으로 정렬
- 최악의 경우: 최고 깊이까지 수행
> Θ(nlogn) 이상 -> 하한 존재 -> Ω(nlogn)
>> 더 좋은 알고리즘 개발해도 시간복잡도 nlogn보다 더 빠르게 할 수 없다
- 리프(Leaf) 노드 n!개
> 트리 깊이 log(n!) 이상: 최소 깊이
- 𝑛P𝑛 = n! ex) 원소 3개 -> 3!-> 6가지

스털링(Stirling) 근사식
- n! ~ ((2𝜋𝑛)^0.5) * (n/e)^n
- ((2𝜋𝑛)^0.5)*(n/e)^n <= n! <= e*(n^0.5)*(n/e)^n
- 양변 log
- nlogn - nloge + log((2𝜋𝑛)^0.5) <=log(n!) <= nlogn - nloge + log(e*(n^0.5))
- log(n!) = Θ(nlogn)
