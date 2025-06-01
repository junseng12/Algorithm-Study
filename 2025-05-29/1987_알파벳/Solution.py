# Problem: 1987_알파벳
# Date: 2025-05-29
# Language: Python 3

# 조건
# 세로 R칸, 가로 C칸으로 된 표 모양의 보드 존재
# 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행, 1열) 에는 말이 놓여 있음
# 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동 가능
# >> 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 함
# 같은 알파벳이 적힌 칸을 두 번 지날 수 없음
# 좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하라(좌측 상단의 칸도 포함)

# 가정
# 첫째 줄: R, C 주어짐 (1 ≤ R,C ≤ 20) 
# 둘째 줄~  (R개의 줄):에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어짐

# 아이디어 : 
# 문제에서 상하좌우로 움직인다고 했으니까, 각 원소에 대해 상하좌우(특정 위치의 인덱스 일부 제한되는 것 제외) 방향성 그래프로 설정함
# dfs 탐색을 통해 조건에 만족하는 발판으로 이동할 수 있는 경우, count ++ 처리 (dfs 처리 시작점 - 좌측 상단으로 고정)
# visited = [] 배열로 방문했던 알파벳 넣어놓고, 있으면 추가하지 않는 것..
# dfs 문제를 많이 풀다 보니까, dfs 처리로 하면 될 것 같다는 느낌인데.. dfs 맞는지 잘 모르겠음..(좀 이전이랑 노드간 연관 관계가 다르다고 느낌)
# 상하좌우 좌표 ([1, 0], [-1, 0], [0, -1], [0, 1]) 이런 느낌으로 
# 


# 🧠 Q1: 문제 상황과 탐색의 구조를 먼저 정리해보자
# 현재 위치에서 출발하여 어떤 조건을 만족하며 이동해야 해?
# 현재 위치에서 출발하며, 인접한 한 칸을 이동하되 동일한 문자가 있는 칸을 지나쳐서는 안되

# 이동할 수 있는 방향과 제한 조건은 어떤 구조야?
# 인접한 상하좌우 칸으로 움직일 수 있어
# >> 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 함

# 어떤 정보를 DFS 상태로 기록해야 할까?
# dfs에는 이전 노드의 위치, 지금까지 밟은 칸의 알파벳 종류 를 기억해야 해

# 🔍 Q2: 핵심 DFS 상태를 정의해보자
# 이 문제에서 DFS에서 다음 3가지를 상태로 가지고 있어야 해:
# 1) 현재 위치 (x, y)
# 2) 지금까지 지나온 알파벳의 집합
# 3) 현재 경로 길이

# 질문:
# Q2-1. visited 배열 대신 어떤 자료구조로 알파벳 사용 여부를 체크하는 게 효율적일까?
#아까 네가 힌트를 줬던 것 같은데.. 동일한 알파벳만 안 지나면 되니까 set 자료구조를 이용해도 될 것 같아.

# Q2-2. DFS 내부에서 백트래킹이 필요한 이유는 무엇일까?
# 지금 지나고 있는 경로의 길이가 최선의 경로 길이가 아닐 수 있기 때문이야.

# Q2-3. DFS는 어떤 조건에서 종료되어야 할까?
# dfs 첫 시작점에서부터 갈 수 있는 모든 경로에 대해 경로 길이를 확인했을 때.. 종료해야지

import sys
from collections import defaultdict
input = sys.stdin.readline

# 1. 재귀 깊이는 여유 있게 10000 정도로만 설정
sys.setrecursionlimit(10000)

# 그래프 구성
graph = defaultdict(list)

R, C = map(int, input().split())

# 1) 문자를 정수 비트(0~25)로 미리 변환
#   board_bits[r][c] = 1 << (ord(board[r][c]) - ord('A'))
board_bits = [None] * R
for r in range(R):
    row = input().rstrip()
    bits_row = [0] * C
    for c in range(C):
        bits_row[c] = 1 << (ord(row[c]) - ord('A'))
    board_bits[r] = bits_row

# 2) 이동 델타 (상, 하, 좌, 우)
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

# memo[x][y]에 visited_mask 저장
visited_memo = [[set() for _ in range(C)] for _ in range(R)]

# 3. 상/하/좌/우 이동 델타
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

answer = 0

def dfs(x, y, depth, visited_mask):
    global answer
    if visited_mask in visited_memo[x][y]:
        return
    visited_memo[x][y].add(visited_mask)
    
    answer = max(answer, depth)
    if answer == 26:
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            next_bit = board_bits[nx][ny]
            if not (visited_mask & next_bit):
                dfs(nx, ny, depth + 1, visited_mask | next_bit)

start_mask = board_bits[0][0]
dfs(0, 0, 1, start_mask)


print(answer)