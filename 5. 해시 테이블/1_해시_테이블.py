
"""
cf)
* Direct-Address Tables
- Direct-Address Tables은 검색, 삽입, 삭제가 빠른 장점이 있다
- 실제 사용하는 공간이 낭비되는 경우가 많다

* 저장 / 검색 시간
- n개의 원소 저장/검색: Θ(𝑛)
- 검색 트리: 평균 Θ(log𝑛) 최악 Θ(𝑛)
- 균형 잡힌 검색 트리: 최악에도 Θ(log𝑛)
- 해시 테이블: 상수 시간
–> 값이 자리를 바로 결정

* 해시 테이블
- 해시 함수로 원소의 해시 값 계산
- key k를 저장할 때 slot k에 저장하는 것이 아니라 slot h(k)에 저장한다
cf)
- Direct-Address Tables에서 공간낭비를 줄이면서도 시간복잡도를 낮추기 위해서 사용
- 충돌문제가 있다 -> Chained Hash Tables: 시간이 느려질 수 있음

* 해시 함수
- 충돌 발생 빈도가 낮아야 한다
- 해시 테이블 사용률이 높아야 한다 (고르게 분포)
- 계산 시간이 빨라야 한다

1. 해시 함수: 나머지 함수
- 해시 테이블 크기 𝑚: 일반적으로는 소수 사용
-> m = 2^p 인 경우 하위 p 비트이므로 고르게 분산되지 않을 수 있다
-> m= 2^p-1 도 피하는 것이 좋음
- h(𝑥) = 𝑥 𝑚𝑜𝑑 𝑚

2. 해시 함수: 곱하기
- 0<𝑎<1 범위의 𝑎
- h(𝑥) = [𝑚×(𝑥×𝑎 𝑚𝑜𝑑 1)]
-> x에 a를 곱한 후 소수점 아래만 얻은 결과에 m을 곱한 후 정수 부분만 얻

3. 해시 함수: 이동 접기 함수(Shift Folding Function)
- 분해->이동->조합
-> 분해: 해시 테이블 크기로 분해
-> 이동 및 조합: 자리 수 넘어가면 잘라 냄

4. 해시 함수: 경계 접기 함수(Boundary Folding Function)
- 분해->이동->조합
-> 분해: 해시 테이블 크기로 분해
-> 이동: 뒤에서부터 한 칸씩 건너뜀 -> 건너뛴 부분 제외하고 숫자를 거꾸로 뒤집음
-> 조합: 자리 수 넘어가면 잘라 냄

5. 해시 함수: 중간 제곱 합수
- (입력 값)^2 -> 중간의 네자리

6. 숫자 분석 기반 해시 함수
- 입력 값들의 분포를 고려
ex) 학번: 앞자리 중복 -> 앞자리 제외

* 문자열 입력
-아스키코드값등사용
1. 첫 번째 문자 이용
–> ABC: 65 (A의 아스키 코드)

2. 문자열 코드 값 더하기
–> ABC: 65 + 66 + 67 = 198
–> 문자 순서 뒤집어도 같은 값이 되므로 취약

3. 자리 수 곱하기
–> ABC: 65x31x31 + 66x31 + 67

* 충돌 해결
1. 체이닝(Chainning)
- 각 버킷에 여러 개의 슬롯: 같은 주소로 해싱되는 원소를 하나의 연결 리스트에 매달아서 관리

2. 개방 주소 방법: 선형 조사법
- 충돌이 발생한 경우 상수 값만큼 증가
- 충돌 발생하면 다음 칸으로: h𝑖(𝑥) = (h(𝑥) + i) 𝑚𝑜𝑑 𝑚
- 특정 영역에 원소가 몰리면 성능이 떨어짐: 한번 충돌난 곳에서 집중적으로 충돌이 남

3. 개방 주소 방법: 제곱 조사법(이차원 조사법)
- 조사 횟수 제곱만큼 증가 h𝑖(𝑥) = (h(𝑥) +i^2) 𝑚𝑜𝑑 𝑚
- 또는 이차 함수만큼 증가 h𝑖(𝑥) = (h(𝑥) + c*i^2 + c*i) 𝑚𝑜𝑑 𝑚
- 초기의 해시 함수 값이 같으면 같은 순서로 이동하므로 여전히 특정 영역에 원소가 몰림

4. 개방 주소 방법: 이중 해싱(더블 해싱)
- 증가 값을 해시로 계산 h𝑖(𝑥) = (h(𝑥) + i*𝑓(𝑥)) 𝑚𝑜𝑑 𝑚
- f(x)에 대해 권장하는 방법
-> m보다 조금 작은 소수 m'
-> f(x) = 1 + (x mod m')
cf)
- h𝑖(x) 함수는 해쉬 테이블의 크기 m과 서로소 관계여야한다 -> 같은 위치 또 갈수도 있음

* 개방 주소 방법
- 주어진 테이블 공간만 사용
-> 적재율이 임계점 이상이면 테이블 크기 두배로
- 삭제의 경우
-> 삭제한 자리 표시(DEL): 찾는 수 없다고 잘못 판단하지 않기 위해
-> 빈 slot이 있는 경우, 원래 값이 있었는데 지워서 비어있는지 아니면 원래 값이 없어서 빈 slot인지 구분x
-> 추가할 때는 DEL 자리에 추가

* 시간 복잡도: 체이닝
- 적재율: 𝛼 = n/m (n: 데이터 개수 / m: 테이블 크기)
- 검색 실패 시 조사 횟수의 기대치: 𝛼
-> 적재율 𝛼
-> 매달린 원소 개수의 기대치 𝛼
-> 평균적으로 𝛼개의 원소를 조사
- 검색 성공 시 조사 횟수의 기대치: 1+ 𝛼/2 - 𝛼/2n
-> 충돌 발생 확률 1/m
-> 찾는 원소 x가 i번째로 추가됨
 -> x보다 나중에 저장되었으면서(x보다 앞) 충돌을 일으킨 원소 개수만큼 조사해야 함
 -> 조사 횟수: 1 + ∑(j:i+1 ~ n)1/m
-> 평균 (1/n)*∑(i:1~n){1 + ∑(j:i+1~n)1/m} =  1+ 𝛼/2 - 𝛼/2n

* 시간 복잡도: 개방 주소 방법
- 적재율 𝛼 = n/m <1
- 검색 실패 시 조사 횟수의 기대치: 최대 1/(1-𝛼)
- 검색 성공 시 조사 횟수의 기대치: 최대 (1/𝛼)*log(1/(1-𝛼))

* 시간 복잡도
- 평균 조사 횟수: 체이닝 < 개방 주소 방법
- 체이닝은 연결 리스트 필요

cf)
- 최악의 경우의 수행시간(Worst Case)
-> 모든 key 값 k가 하나의 slot으로 해슁되는 경우 길이가 n인 이중 연결 리스트가 생성
-> 해쉬 테이블이 아닌 일반적인 리스트에 저정하는 것과 성능이 동일
"""
