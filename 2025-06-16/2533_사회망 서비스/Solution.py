# Problem:  2533_사회망 서비스
# Date: 2025-06-16
# Language: Python 3

# 조건
#  얼리 아답터(early adaptor): 어떤 새로운 아이디어를 먼저 받아들인 사람
# 사회망 서비스에 속한 사람들은 얼리 아답터이거나 얼리 아답터가 아니다. 
# 얼리 아답터가 아닌 사람들은 자신의 모든 친구들이 얼리 아답터일 때만 이 아이디어를 받아들임

# 어떤 아이디어를 사회망 서비스에서 퍼뜨리고자 할 때, 
# 가능한 한 최소의 수의 얼리 아답터를 확보하여 모든 사람이 이 아이디어를 받아들이게 하는 문제

# 일반적인 그래프에서 이 문제를 푸는 것이 매우 어렵다는 것이 알려져 있기 때문에, 
# 친구 관계 그래프가 트리인 경우, 
# => 즉 모든 두 정점 사이에 이들을 잇는 경로가 존재하면서 사이클이 존재하지 않는 경우만 고려함

## 친구 관계 트리가 주어졌을 때, 모든 개인이 새로운 아이디어를 수용하기 위하여 필요한 최소 얼리 어답터의 수를 구하라

# 가정
# 첫 번째 줄: 친구 관계 트리의 정점 개수 N (2 ≤ N ≤ 1,000,000)
# 각 정점은 1부터 N까지 일련번호로 표현

# 두 번째 줄~ (N-1개의 줄): 각 줄마다 친구 관계 트리의 에지 (u, v)

# 아이디어 : 
# 트리 구조에서 정의함(보니까 노드 1번을 루트로 설정하고 시작하면 될 듯)
# 본인과 인접한 모든 노드들이 얼리어답터여야 새로운 아이디어를 수용할 수 있음
# 가능한 최소 노드로 얼리어 답터가 아닌 모든 사람들이 새로운 아이디어를 수용하게 만들려면... 
# 일단 가장 많이 노드들과 인접한 노드부터 얼리어답터로 설정하는 것이 최소 노드에 도달하는 빠른 길 아닌가?
# DP 적 관점으로 밖에 생각이 안남

# 트리 구조로부터 뽑을 수 있는 조건 구조
# 노드가 얼리어답터 X → 자식 노드는 얼리어답터여야 조건 충족
# 노드가 얼리어답터 O → 자식 노드는 자유롭게 선택 가능


import sys
from collections import defaultdict

# 그래프 구성
graph = defaultdict(list)

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N = int(input())

dp = [[0 for col in range(2)] for row in range(N+1) ]

# 양방향 간선 연결 (트리이므로 방향 없음)
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(node, parent):
  dp[node][0] = 0  # 내가 얼리어답터 ❌
  dp[node][1] = 1  # 내가 얼리어답터 ⭕
    
  for child in graph[node]:
    if child == parent:
      continue
  
    dfs(child, node)
    
    dp[node][0] += dp[child][1]
    dp[node][1] += min(dp[child][0], dp[child][1])
    
    
dfs(1, 0)

print(min(dp[1][0], dp[1][1]))