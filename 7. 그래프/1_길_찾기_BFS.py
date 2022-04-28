# 길 찾기: 너비 우선 탐색 BFS
import collections

class Queue(object):
    def __init__(self):
        self.elements = collections.deque()
    def length(self):
        return len(self.elements)
    def push(self, x):
        self.elements.append(x)
    def pop(self):
        return self.elements.popleft()

grid = [[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
        [ 0, 1, 1, 1, 1, 1, 1, 1, 1, 0 ],
        [ 0, 1, 0, 0, 0, 0, 1, 0, 1, 0 ],
        [ 0, 1, 1, 1, 1, 0, 1, 0, 1, 0 ],
        [ 0, 0, 1, 0, 1, 0, 1, 1, 1, 0 ],
        [ 0, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]]  # 벽: 0, 길: 1

for line in grid:  # 지도 그리기
    print(*['#' if x == 0 else '.' for x in line])  # *: 스프래드 연산자: list 그대로 print X -> list의 항목 다 분리해서 print

start = (1, 5)  # (column, index)
goal = (8, 1)

queue = Queue()
queue.push(start)
came_from = {}  # 경로 기록
# 경로 너비 우선 탐색
while queue.length() > 0:  # 비어있지 않으면
    current = queue.pop()  # dequeue: 하나 꺼냄
    if current == goal:
        break
    (x, y) = current
    candidates = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]  # 오른쪽, 아래, 왼쪽, 위
    for next in [(h, v) for h, v in candidates if grid[v][h] != 0]:
        if next not in came_from:  # 방문 안했으면
            queue.push(next)  # enqueue
            came_from[next] = current  # (next):(current), current->next로 옴
# 경로 역추적
current = goal
path = []
while current is not start:
    path.append(current)
    current = came_from[current]
path.reverse()
print(path)
