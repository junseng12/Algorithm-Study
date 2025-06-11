# Problem: 1922_네트워크 연결
# Date: 2025-06-11
# Language: Python 3

# 조건
# 각 컴퓨터를 연결하는데 필요한 비용 주어졌을 때 모든 컴퓨터를 직접 연결하는데 필요한 최소비용 출력하라
# 모든 컴퓨터를 연결할 수 없는 경우는 없음

# 가정
# 첫째 줄: 컴퓨터의 수 N (1 ≤ N ≤ 1000)
# 둘째 줄: 연결할 수 있는 선의 수 M (1 ≤ M ≤ 100,000)
# 셋째 줄~ (M+2번째 줄): 총 M개의 줄에 각 컴퓨터를 연결하는데 드는 비용 a, b, c (a컴퓨터와 b컴퓨터를 연결하는데 비용이 c (1 ≤ c ≤ 10,000) 만큼 듦)
# a와 b는 같을 수도 있음(Why? 같은 컴퓨터는 연결할 필요가 없잖어..)

# 아이디어 : 
# 딱봐도 MST 문제이며, 최소 비용 구상하는 문제
# 어떤 알고리즘을 이용하여 풀 것인지 고려해야 함
# 크루스칼 : O(E log E), 프림 : O(V^2) (간선 많을 때 힙 사용하면 - O(E log V))
# 지금은 간선이 그렇게 많지 않은 편이라고 판단되어 10^5 정도 -> 크루스칼 알고리즘 선택


import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N = int(input())
M = int(input())

#Kruskal 알고리즘에서 일반적으로 간선 오름차순 정렬하는 방법 - sort()
edges = [] # 간선 목록 (가중치, u, v)
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()  # 가중치 기준으로 정렬 (heapq 없이 그냥 sort())

# 직접 써보기
total_weight = 0 # MST의 총 가중치 합
edge_count = 0 # MST에 포함된 간선 수

parent = [i for i in range(N+1)]

def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]
  
def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root  # 또는 rank 기준으로 최적화 가능


def Kruskal ():
  global total_weight
  global edge_count
  
  for w, u, v in edges:
    if find(u) != find(v):
      union(u, v)
      total_weight += w
      edge_count += 1
      
      if (edge_count == N-1): 
        break
  
    
Kruskal()

print(total_weight)