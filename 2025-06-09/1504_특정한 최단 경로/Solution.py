# Problem: 1504_특정한 최단 경로
# Date: 2025-06-09
# Language: Python 3

# 조건
# 방향성이 없는 그래프
# 1번 정점에서 N번 정점으로 최단 거리로 이동(두 가지 조건을 만족하면서 이동하는 특정한 최단 경로)
# 임의로 주어진 두 정점은 반드시 통과해야 한다
  # 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있음(하지만 반드시 최단 경로로 이동)

# 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하라


# 가정
# 첫째 줄: 정점의 개수 N, 간선의 개수 E(2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000)
# 둘째 줄부터 (E개의 줄): 세 개의 정수 a, b, c(a번 정점에서 b번 정점까지의 양방향 길, 그 거리 c) (1 ≤ c ≤ 1,000)
# 다음 줄: 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2 (v1 ≠ v2, v1 ≠ N, v2 ≠ 1)
# 임의의 두 정점 u와 v사이에는 간선이 최대 1개 존재

# 아이디어 : 
# 1번 정점에서 N번 정점으로 최단 거리 ->  (Dijkstra 알고리즘)
# 두 가지 조건 존재
# 임의로 주어진 두 정점은 반드시 통과
# 1번 정점에서 N 번 정점 사이의 최단 거리 계산
# >>  이것을 만족할 때 최단 거리 Update& 종료 가능

# 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있음
# visited 배열 처리하면 안 될 듯함.. 근데, 그러면 1번과 N 번 정점 지났는지... v1, v2 지났는지는 어떻게 판별하지..? 
# 아 visited 배열 처리해도, 조건문에 필터링하는 내용으로 visited 안보면 될 듯
# visited 배열 처리해야 함


# Q1-1. 문제에서 요구하는 최종 목표는 무엇인가?
# (정확히 어떤 "경로의 최단 거리"를 구해야 하는가?)
# 1번 정점에서 N 번 정점까지의 최단 거리를 구해야 함

# Q1-2. 이번 문제에서 "단일 Dijkstra로는 해결이 불가능한 이유"는 무엇인가?
# (왜 Dijkstra 1번만으로 모든 것을 구할 수 없는지 생각해보자)
# 단일 Dijkstra는 1->N 까지의 중복된 거리 없고, 지나야 하는 정점 조건 없이 최단 거리를 구하기 때문임

# Q1-3. Dijkstra를 몇 번 실행해야 할까?
# (시작 노드부터, 중간 노드까지, 이런 식으로 생각해볼 수 있음)
# 네가 말해준 것부터 느낌이 왔는데,, 1번 정점으로부터 v1 정점까지의 최단 거리, v1 정점으로부터 v2 정점까지의 최단 거리, v2 정점으로부터 N 정점으로까지의 최단 거리 이렇게 나누면 될 듯
# 다만, 1 -> v2, 1->v1 이 두 가지의 경우에 무엇이 더 최단 거리인지 비교해봐야 할 듯

# Q1-4. "INF 처리"는 어디서 신경써야 할까?
# (경로가 존재하지 않는 경우 처리 방법은?)
# 처음 초기화할 때 모든 경로에 대해 INF 처리하여 최단 거리를 기록하고 업데이트하도록 설정함
# 없는 경로에대해서는 아마 INF 그대로 초기값 남아있지 않을까? 더 신경써야 할 부분이 있는지 모르겠음

# Q1-5. 이 문제에서 Dijkstra의 distance 배열은 어떤 역할을 할까?
# (이번엔 여러 번 Dijkstra를 돌릴 때 distance 배열을 어떻게 활용할 것인지도 생각해보자)
# 한번 distance 배열을 처리하고 나면, 다른 전역 변수에 총 길이를 저장하고 이 distance 배열은 0으로 초기화하여 다시 부분 경로에 따른 distance 계산하는 방식으로 진행하면 될듯


import sys
from collections import defaultdict
import heapq
import math

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N, E = map(int, input().split())

graph = defaultdict(list)

# 양방향 간선 연결(weight도 이용해야 하므로, 연결된 노드와 weight를 튜플 형태로 저장)
for _ in range(E):
  u, v, weight = map(int, input().split())
  graph[u].append((v, weight))
  graph[v].append((u, weight))
  
v1, v2 = map(int, input().split())

def dijkstra(start):
  distance = [math.inf for _ in range(N+1)]
  queue = []
  heapq.heappush(queue, (0, start))
  distance[start] = 0
  
  while queue:
    current_distance, current_node = heapq.heappop(queue)

    if current_distance > distance[current_node]:
        continue
      
    for adj_node, weight in graph[current_node]:
      if distance[adj_node] > current_distance + weight:
        distance[adj_node] = current_distance + weight
        heapq.heappush(queue, (distance[adj_node], adj_node))

  return distance


# 1 -> v1 or v2
d1 = dijkstra(1)
# v1 -> v2 or N
d2 = dijkstra(v1)
# v2 -> v1 or N
d3 = dijkstra(v2)

# 경로1 = d1[v1] + d2[v2] + d3[N]
# 경로2 = d1[v2] + d3[v1] + d2[N]
route1 = d1[v1] + d2[v2] + d3[N]
route2 = d1[v2] + d3[v1] + d2[N]
# if INF 체크 → -1 출력
# else → min(경로1, 경로2) 출력



if (route1 == math.inf) or (route2 == math.inf):
  print(-1)
else:
  print(min(route1, route2))
  
  
