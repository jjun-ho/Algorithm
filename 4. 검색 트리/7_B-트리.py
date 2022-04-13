
"""
* B-트리(B-Tree)


* B* 트리
- 각 노드에 값 많이 저장하도록 함 (노드의 높이 줄이기 위함)
- 루트 노드가 아니면 최대 저장 공간의 2/3 이상 자료가 저장되어야 함
- 노드에 저장된 자료가 넘치는 경우 형제 노드로 재분배
- 모든 형제 노드가 가득찼을 때만 분할


* 시간 복잡도
- 균형 이진 검색 트리 깊이: log(2)𝑛
- 균형 d진 검색 트리 깊이: log(d)𝑛
- B-트리 깊이: log(d/2)𝑛 ~ log(d)𝑛
- B-트리 추가, 삭제, 검색: 𝑂(log𝑛)
–> 이진 검색 트리에 비해 상수 인자가 작음
"""