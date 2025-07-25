# Problem:  1240_노드 사이 거리
# Date: 2025-06-18
# Language: Python 3

# 조건
# N개의 노드로 이루어진 트리
# M개의 두 노드 쌍을 입력받음
# 두 노드 사이의 거리를 출력

# 가정
# 첫째 줄: 노드의 개수 N, 거리를 알고 싶은 노드 쌍의 개수 M
# 다음 ~ (N-1개의 줄): 트리 상에 연결된 두 점과 거리를 입력받음 
# 그 다음 줄: 거리를 알고 싶은 M개의 노드 쌍이 한 줄에 한 쌍씩 입력됨

# 2≤N≤1000, 1≤M≤1000 
# 트리 상에 연결된 두 점과 거리는 10000 이하인 자연수
# 트리 노드의 번호 1~ N까지의 자연수
# 두 노드가 같은 번호를 갖는 경우 없음


# 출력 : M개의 줄에 차례대로 입력받은 두 노드 사이의 거리

# 아이디어 : 
# 그래프에서 두 노드 간 최단 거리와 비슷한 관점으로 풀이할 수 있을 것 같음
# 결국 여기서 최단 거리가 곧 두 점 사이의 거리로 이어지니까?

# 가중치가 있는 그래프에서 최단 거리를 구하려고 한다면 다익스트라 알고리즘, 플로이드-워셜 알고리즘 중 하나
# 다익스트라 알고리즘을 직접 구현해본 적이 있었던 것 같은데.. 자료구조 찾아보니 다익스트라 알고리즘이 가장 효율적일 것으로 판단하고 구현하고자 함
# 해당 알고리즘 로직 상 가중치가 중요하여 양방향 간선 추가 시에 weight도 같이 저장


## 핵심 >>> 문제 구조상 자료구조가 트리이므로, 어차피 사이클은 존재하지않고 DFS 만으로 효율적을 처리 가능
## dfs 이용하여 문제 재풀이 진행


import sys
from collections import defaultdict

# 그래프 구성
graph = defaultdict(list)

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())


# 양방향 간선 연결(weight도 이용해야 하므로, 연결된 노드와 weight를 튜플 형태로 저장)
for _ in range(N-1):
  u, v, weight = map(int, input().split())
  graph[u].append((v, weight))
  graph[v].append((u, weight))


visited = [False] * (N+1)
dist = [0 for _ in range(N+1)]

def dfs(current, target, distance):
    visited[current] = True
    dist[current] = distance
    if current == target:
        return
    for adj, weight in graph[current]:
        if not visited[adj]:
            dfs(adj, target, distance + weight)
  

for _ in range(M):
    start, target = map(int, input().split())
    visited = [False] * (N+1)
    dist = [0] * (N + 1)
    dfs(start, target, 0)
    print(dist[target])