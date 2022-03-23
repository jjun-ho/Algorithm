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