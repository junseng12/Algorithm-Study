# Problem: 14752_Map Labeling
# Date: 2025-07-18
# Language: Python 3

# 조건
# N행 M열의 격자
# 각 칸에 알파벳이 써있고 환형으로 이어짐 [왼쪽 위를 (1, 1), 오른쪽 아래를 (N, M)]

# 아무 곳에서나 시작해서 상하좌우나 대각선 방향의 칸으로 한 칸씩 이동 가능 (이 때, 이미 지나 왔던 칸들을 다시 방문하는 것은 허용)
# 시작하는 격자의 알파벳을 시작으로, 이동할 때마다 각 칸에 써진 알파벳을 이어 붙여서 문자열 생성 가능

# 문자열을 K 개 알려주면, 각 문자열 마다 만들 수 있는 경우의 수 계산.
# 경우의 수를 셀 때, 방문 순서가 다르면 다른 경우이다. 즉, (1,1)->(1,2) 로 가는 것과 (1,2)->(1,1) 을 가는 것은 서로 다른 경우

# 환형 개념
#1행에서 위로 가면 N 행으로 가게 되며 반대도 가능하다.
#1열에서 왼쪽으로 가면 M 열로 가게 되며 반대도 가능하다.
# 대각선 방향에 대해서도 동일한 규칙이 적용된다.
# ex) (1, 1)에서 위로 가면 (N, 1)이고, 왼쪽으로 가면 (1, M)이며 왼쪽 위 대각선 방향으로 가면 (N, M)인 것

# 격자의 정보와, K 개의 문자열이 주어졌을 때, 각 문자열 마다 만들 수 있는 경우의 수 계산하라

# 가정
# 3 ≤ N, M ≤ 10, N과 M은 자연수
# 1 ≤ K ≤ 1,000, K는 자연수
# 1 ≤ 문자열의 길이 ≤ 5
# 문자열은 중복될 수도 있음

## 입력 ##
# 첫번째 줄: 격자의 크기 N X M, 문자열의 개수 K
# ~N개의 줄: M개의 알파벳 소문자가 공백없이 주어짐. (첫 번째 줄은 1행의 정보이며, N 번째 줄은 N행의 정보)
# ~이어서 K개의 줄: 문자열 (모두 알파벳 소문자)


## 출력 ## 
# ~K개의 줄: 문자열을 만들 수 있는 경우의 수 순서대로 출력


# 아이디어 
# 이전 문자열 문제처럼...
# board 내 임의 시작점에서 돌아가면서 중복 움직임 허용하며, dfs 처리를 통해 문자열 만들어감(범위를 넘어가는 이동이 될 수 있는데.. 그때는 modular 연산으로 환형으로 돌아가도록)
# 문자열은 바로 Trie에 삽입함(중복된 문자열이 들어오면 어떻게 처리할 것인가? - 만약, 최종 출력값에 dict 형태로 기록할 수 있으면 dict 미리 확인 후 없는 데이터에 대해서만 dfs 처리하고 출력하도록)

# dfs 정의
# dfs 내 전달 요소 : 위치값 x y, depth(문자열 길이 <= 5), 현재 만들어진 문자열(s)
# dfs 종료 조건 : depth == MAX_LEN(5)


import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import defaultdict

# dfs 함수 설계 - 현재 (x, y) 위치에서, Trie를 따라가며 가능한 모든 단어를 탐색
def dfs(x, y, depth, s):
    # 8 개 방향 : 상, 하, 좌, 우, 좌상, 우상, 우상, 우하
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    # 중복 방문이 가능하여 visited 배열 없어도 될 듯함
    # if visited[x][y] :
    #     return
    count_map[s] += 1
    
    # (종료조건) 길이 제한
    if depth == max_query_len:
        return
    
    # visited[x][y] = True
    for dir in range(8):
        # (-1, -1) 이 인덱스 범위 넘어서면 mod 연산하여 다시 (N, M)로 이동되도록 설정
        nx = (x + dx[dir] + N) % N   # wrap-around
        ny = (y + dy[dir] + M) % M
        dfs(nx, ny, depth + 1, s + board[nx][ny])


# main 함수로 구분지으려다가 자꾸 전역 변수 선언하기 어려워져서 그냥 다 전역으로 처리하겠음
# Map 자료 구조 활용(dfs 처리한 결과를 map 자료구조에 다 기록함)
count_map = defaultdict(int)

# 단어 사전 내 단어의 수 입력받기
N, M, K = map(int, input().split())    
    
# N X M board 2차원 배열 선언 및 입력깂 받기
board = [list(input().rstrip()) for _ in range(N)] # [['A','C','M','A'],...,]

queries = [input().strip() for _ in range(K)]
max_query_len = max(len(q) for q in queries)   
        
# board 내 첫 출발점 잡기 - 모든 칸이 출발점이 될 수 있음
for x in range(N):
    for y in range(M):
        string = board[x][y]
        dfs(x, y, 1, string)
        
for q in queries:
    print(count_map.get(q, 0))

                
