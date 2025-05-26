# Problem: 13023_ABCDE
# Date: 2025-05-26
# Language: Python 3

# 조건
# 캠프에 총 N명이 참가하고 있음
# 사람들은 0번부터 N-1번으로 번호가 매겨져 있고, 일부 사람들은 친구임
# 다음과 같은 관계를 가진 사람 A, B, C, D, E 존재하는지 구하는 프로그램 
# - A는 B와 친구다.
# - B는 C와 친구다.
# - C는 D와 친구다.
# - D는 E와 친구다.


# 가정
# 첫 줄 : 사람의 수 N (5 ≤ N ≤ 2000), 친구 관계의 수 M (1 ≤ M ≤ 2000)
# 둘째 줄~(M개의 줄): 정수 a와 b가 주어지며, a와 b가 친구라는 뜻이다. (0 ≤ a, b ≤ N-1, a ≠ b) 
# 같은 친구 관계가 두 번 이상 주어지는 경우는 없음

# 문제의 조건에 맞는 A, B, C, D, E가 존재하면 1을 없으면 0 출력

# 아이디어 : 
# 사이클이 형성될 수도 있는 그래프 구조인 듯함
# 그런데, 단순 사이클 체크가 아니라, 사이클 구조를 이루는 원소가 5개여야 함
# 사이클 체크하면서, 사이클이 존재한다면, 그 사이클을 이루는 원소의 개수를 확인해야 함
# 사이클 확인은... dfs 처리하다가 어떻게 확인하면 될까..?
# 왠지 dfs 처리하면서 dfs로 넘어갈 때마다, +1 씩 추가하면서 +5인 사이클이 있다면..! 1을 출력함

# >> 문제 자세히 보니까 사이클 구조가 아님
# 단순 A -> B -> C -> D -> E 이렇게 5개가 연결된 것이 있는지 확인하는 것


### 🔍 Q1. **문제의 본질은 무엇인가?**

# > ✔️ **친구 관계 그래프**에서 A-B-C-D-E,  
# > 즉 **길이 4(노드 5개)**의 **단순 경로가 존재하는지**를 판단하는 문제

# - 조건: 같은 노드를 다시 방문하지 않고, **총 5개의 노드가 연결된 길이 4의 경로**
# - 출력: 경로가 존재하면 1, 아니면 0

# ---

# ### 📌 핵심 제약 조건

# - **일반 무방향 그래프** (트리 아님!)
# - 간선 수 최대 2000개 → **시간복잡도 O(N\*DFS-depth) 허용됨**
# - 완전 탐색을 해도 시간 초과 없음


import sys
from collections import defaultdict
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

# 그래프 구성
graph = defaultdict(list)

N, M = map(int, input().split())

# 양방향 간선 연결)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(N)]
# 깊이 5인 (노드 5개로 이루어진) 관계 존재하는지 여부 확인 
isexist = 0


def dfs(node, depth):
    global isexist
    if (depth == 5):
        # isexist = 1
        # return
        print(1)
        # 더욱 간편하게 처리하는 방법
        exit(0)
    visited[node] = True
    for next_node in graph[node]:
        if visited[next_node] != True:
            dfs(next_node, depth + 1)
            # #dfs 재귀 호출 처리하다가 return 되어 돌아왔다면, 이후의 처리는 진행할 필요 없음
            # if isexist:
            #     return
    visited[node] = False


for i in range(N):
    dfs(i, 1)
    if isexist:
        break
          
print(0)