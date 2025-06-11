# Problem: 1647_도시 분할 계획
# Date: 2025-06-11
# Language: Python 3

# 조건
# 마을 - N개의 집, 그 집들을 연결하는 M개의 길
# 각 길마다 길을 유지하는데 드는 유지비
# 마을의 이장은 마을을 두 개의 분리된 마을로 분할할 계획(두 개의 트리구조로 분리)
# 각 분리된 마을 안에 집들이 서로 연결되도록 분할
# 마을에는 집이 하나 이상 있어야 함

# 분리된 두 마을 사이에 있는 길들은 필요가 없으므로 없앨 수 있음
# 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨 수 있음

#위 조건을 만족하도록 길들을 모두 없애고 나머지 길의 유지비의 합을 최소로 하자

# 가정
# 첫째 줄: 집의 개수 N, 길의 개수 M (N은 2이상 100,000이하인 정수, M은 1이상 1,000,000이하인 정수)
# 그 다음 줄부터 ~(M개의 줄): 길의 정보 A B C 주어짐 (A번 집과 B번 집을 연결하는 길의 유지비가 C (1 ≤ C ≤ 1,000))

# 아이디어 : 
# 연결된 자료 구조를 두 개의 MST 구조로 나누어야 함
# 생각해봤을 떄.. 서로 다른 두 개의 MST 구조로 나눌 때 결국, 간선의 최소합을 유지하게 하면서 두 개의 집단을 나누어야 하므로, 간선을 기준으로 집단을 나눠야 함
# Kruskal 알고리즘에 따라, 처리하면서 간선에 따라 연결되면 결국, 노드끼리도 서로 다른 MST 집단에 속하게 될 것임

# 그럼... 매번 최소 간선을 선택하면서.. MST를 신장하게 될 텐데... 
# 그냥 MST를 하나 생성하고 그 생성한 MST에 포함된 간선 중에 가장 큰 가중치를 가진 간선만 제거하면 가장 최소의 가중치의 합을 가진 MST 2개로 분할 가능함 
# 결국 간단하게 남은 길 유지비의 합의 최솟값만 출력한다면.. 그 MST 신장할 떄마다 가중치 w 를 기억해서 가장 큰 가중치 값을 전체 MST의 Total 가중치 값에서 빼주면 됨


import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

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

MST_edge = []

def Kruskal():
  global total_weight
  global edge_count
  global MST_edge
  
  for w, u, v in edges:
    if find(u) != find(v):
      union(u,v)
      total_weight += w
      edge_count += 1
      
      MST_edge.append([w, u, v])
      
      if edge_count == N - 1:
        break


Kruskal()

target_edge = max(w for w, u, v in MST_edge)

print(total_weight - target_edge)