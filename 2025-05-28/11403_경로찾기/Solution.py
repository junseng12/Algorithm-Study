# Problem: 11403_경로찾기
# Date: 2025-05-28
# Language: Python 3

# 조건
# 가중치 없는 방향 그래프 G 가 주어짐
# 모든 정점 (i, j)에 대해, i -> j 로 가는 길이가 양수인 경로가 있는지 없는지 구하라

# 가정
# 첫 줄 : 정점의 개수 N (1<= N <= 100)
# 둘째 줄 ~  (N개 줄) : 그래프의 인접 행렬
# i번쨰 줄의 j 번쨰 숫자가 1 => i->j 로 가는 간선이 존재함 (0인 경우는 간선이 없음)
# i번째 줄의 i 번째 숫자는 항상 0 임

# 아이디어 : 
# 결국 특정 i에 대해 모든 방향 그래프를 dfs 방식으로 탐색하여, 도달할 수 있는 모든 노드를 확인하고 기록한다
# for 반복문 내 각 i마다 dfs 처리하면서, i -> j 에 해당하는 것을 찾았을 경우 임시 matrix에 기록함



# ## 🧠 Q1. 이 문제는 어떤 그래프 탐색의 본질을 묻고 있을까?

# * N개의 노드로 구성된 **방향 그래프**가 주어진다.
# * `i → j` 경로가 존재하는지 여부를 **모든 노드 쌍**에 대해 출력해야 한다.

# 🔍 Q1 힌트:
# - “한 번이라도 도달할 수 있다면 1, 아니라면 0”을 출력해야 함.
# - 단순 DFS로 하나하나 확인할 수도 있지만,
# - 모든 노드쌍을 검사해야 하므로 시간복잡도 고려가 필요해.

# 💡 어떤 접근법이 가장 적절해 보이는가?

# ## 💬 감각 체크 유도

# 1. 이 문제는 "모든 노드 간 도달 가능 여부"를 묻고 있음 → 무엇이 떠오르나?
# 2. DFS를 N번 돌리면 어떻게 될까? 시간은 괜찮을까?
# 3. 이 구조, 혹시 **플로이드 와샬(Floyd-Warshall)** 알고리즘과 유사하지 않나?


import sys
from collections import defaultdict
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

# 그래프 구성
graph = defaultdict(list)

N = int(input())

adj_matrix = [list(map(int, input().split())) for _ in range(N)]

# 인접 리스트 변환
for i in range(N):
    for j in range(N):
        if adj_matrix[i][j] == 1:
            graph[i].append(j)
            
# 결과 저장
tmp_matrix = [[0 for _ in range(N)] for _ in range(N)]

def dfs(start, node):
    for nxt in graph[node]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(start, nxt)
        if nxt == start:
            tmp_matrix[start][start] = 1  # 자기 자신으로 돌아옴
        tmp_matrix[start][nxt] = 1


            
for i in range(N):
    visited = [False for _ in range(N)]
    dfs(i, i)
        
for row in tmp_matrix:
    print(' '.join(map(str, row)))
    
    
    