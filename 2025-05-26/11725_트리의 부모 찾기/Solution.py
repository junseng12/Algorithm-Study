# Problem: 11725_트리의 부모 찾기
# Date: 2025-05-26
# Language: Python 3

# 조건
# 루트 없는 트리가 주어짐
# 트리 루트 1이라 정했을 때, 각 노드의 부모를 구하는 프로그램 작성 

# 가정
# 첫 줄 : 노드의 개수 N (2 ≤ N ≤ 100,000)
# 둘째 줄부터 ~(N-1개의 줄): 트리 상에서 연결된 두 정점

# 아이디어 : 
# 어차피 DFS 처리하면, 특정 노드를 루트로 설정한 것에서부터 부모노드로 설정되어 탐색 진행함
# 따라서 DFS 재귀 호출하여 처리하기 전, 해당 부모 노드를 기록해놓으면 될 듯

import sys
from collections import defaultdict
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

# 그래프 구성
graph = defaultdict(list)

N = int(input())

# 양방향 간선 연결(가중치도 이용해야 하므로, 연결된 노드와 가중치를 튜플 형태로 저장)
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


parent = [ 0 for _ in range(N+1)]

def dfs(node):
    for next_node in graph[node]:
        if parent[next_node] == 0:
            parent[next_node] = node
            dfs(next_node)

# 만약 인접한 노드1(루트 노드)을 들렸을 때, 노드 1을 기준으로 다시 dfs처리되지 않게 하기 위함
parent[1] = -1

dfs(1)

for i in range(2, N+1):
    print(parent[i])
