# Problem: 1753_최단경로
# Date: 2025-06-07
# Language: Python 3

# 조건
# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로 구하라
# 단, 모든 간선의 weight는 10 이하의 자연수

# 가정
# 첫째 줄: 정점의 개수 V, 간선의 개수 E (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000)
# 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정

# 둘째 줄: 시작 정점의 번호 K(1 ≤ K ≤ V)
# 셋째 줄~ (E개의 줄): 각 간선을 나타내는 세 개의 정수 (u, v, w) 순서대로 주어짐(u에서 v로 가는 weight w인 간선이 존재함)

# u와 v는 서로 다르며 w는 10 이하의 자연수
#서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음


## 출력 
#첫째 줄~ (V개의 줄): i번째 줄에 i번 정점으로의 최단 경로의 경로값
# 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF 출력

# 아이디어 : 
# 한 출발 정점에서 다른 정점으로의 모든 경로 계산 필요(dfs 방식 - 최단 경로인 것 같으면 업데이트)
# 솔직히 BFS인지 DFS인지 잘 모르겠다..
# 최단 경로다 보니 가까운 정점을 들리는 게 맞을 수도 있을 것 같은데..

# 타겟 노드 존재, 갔던 노드가 타겟 노드가 아니라면..더 나아가서 
# 1) 타겟 노드와 직접 연결된 경우
#  - 타겟 노드와 연결되어 있는 간선 weight(weight 낮은 것 선택)만큼 바로 거리 업데이트
# 2) 타겟 노드와 직접 연결되지 않은 경우
#  - 임의 간선 선택한 다음에, 타겟 노드와 연결된 간선이 있는지 탐색(BFS 느낌나는데?)
#  - 또 없으면, 이전으로 돌아가서 다음 임의 간선 선택해서 타겟 노드와 연결된 간선 있는지 탐색(만약에 있으면, 최단 경로 업데이트도 진행하고)



# 문제: 
# 가장 depth가 가까운 것이 최단 거리 보장하지 않음
# 두 정점 사이의 여러 간선 존재할 수 있음 - 무조건 더 작은 weight 경로를 선택해야 하는데.. (그 판단 기준을 어떻게?)

# 양방향 그래프

# 시작점인지 판단 하고 시작점이면 0 출력



# 기저 조건
# BFS 모든 탐색 완료했을 때?


# ✅ Q1 단계 — 사고 흐름 유도 질문
# Q1-1. 문제의 본질적인 목표는 무엇인가?
# (ex: 무엇을 구하고자 하는가?)
# 시작 V 로부터 다른 모든 정점 간의 각각의 최단 경로

# Q1-2. 입력으로 주어지는 그래프는 어떤 성질을 가지는가?
# (유향 / 무향, weight 유무 등)
# 무향 그래프이고, weight 존재함

# Q1-3. 최단 경로 문제에서 BFS가 아닌 Dijkstra를 사용하는 이유는 무엇인가?
# Q1-4. Dijkstra 알고리즘에서 어떤 자료구조를 사용하면 효율적인가?
# (왜 그 자료구조가 필요한가?)
# DFS랑 BFS 고민하다 BFS 처리하면 될 것 같다고 생각했는데.. 
# 다익스트라 알고리즘 잘 몰라서 BFS 고민하여 풀었음

# Q1-5. Dijkstra 알고리즘 구현 시 다음 중 무엇을 관리해야 하는가?
# 각 노드까지의 현재까지 발견된 최단 거리
# length 변수에 기록해놓는다. 최단 거리 새로 발견하면 업데이트하기

# 이미 처리한 노드 여부
# 이게 헷갈린다.. 이미 처리한 노드를 놔두고 안 처리한 노드와의 K 노드 간 최단 거리를 구할 때, 또 이미 처리한 노드를 거쳐 갈 수도 있다 보니 .. 어려움

# (이 2가지 정보를 어떻게 관리할지 생각해보자)



import sys
from collections import defaultdict
import heapq
import math

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


V, E = map(int, input().split())
K = int(input())


graph = defaultdict(list)

# 단방향 간선 연결(weight도 이용해야 하므로, 연결된 노드와 weight를 튜플 형태로 저장)
for _ in range(E):
    u, v, weight = map(int, input().split())
    graph[u].append((v, weight))
    # graph[v].append((u, weight))
    

distance = [math.inf for _ in range(V+1)]
distance[K] = 0

queue = []
heapq.heappush(queue, (0, K))

while queue:
    current_distance, current_node = heapq.heappop(queue)
    
    if current_distance > distance[current_node]:
        continue
    
    for adj_node, weight in graph[current_node]:
        if distance[adj_node] > current_distance + weight:
            distance[adj_node] = current_distance + weight
            heapq.heappush(queue, (distance[adj_node], adj_node))



for i in range(1, V+1):
  if distance[i] == math.inf:
    print("INF")
  else: 
    print(distance[i])