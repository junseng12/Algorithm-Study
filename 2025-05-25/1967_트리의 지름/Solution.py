# Problem: 1967_트리의 지름
# Date: 2025-05-25
# Language: Python 3

# 조건
# 트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것
# 이때, 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 됨 => 트리의 지름
# 트리의 지름 : 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이
# 입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하라 

# 가정
# 첫 줄: 노드의 개수 n(1 ≤ n ≤ 10,000)
# 둘째 줄~: n-1개의 줄에 각 간선에 대한 정보 (간선에 대한 정보는 세 개의 정수로 이루어져 있음)
# 세 개의 정수 구성 : 첫 번째 정수(간선이 연결하는 두 노드 중 부모 노드의 번호), 두 번째 정수(자식 노드), 세 번째 정수(간선의 가중치)

# 간선 입력 순서 있음(부모 노드의 번호가 작은 것이 먼저 입력되고, 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력됨)
# 루트 노드의 번호는 항상 1이라고 가정
# 가중치(100보다 크지 않은 양의 정수)

# 아이디어 : 
# 사이클이 없는 무방향 그래프
# 목적 - 가장 큰 가중치의 합을 가진 두 노드 간 연결
# 
# 이것을 조건 분기로 생각을 잘 못했는데.. 잘 보면.. 루트 노드인 1번 노드 입장에서.. 
# dp[node][0] = node 기준 왼쪽의 서브 트리의 가중치 최대 합,
# dp[node][1] = node 기준 오른쪽의 서브 트리의 가중치 최대 합
# 이렇게 정의할 수 있지 않을까?

# dp[node][0] = weight[node][0] + max(dp[leftchild][0], dp[leftchild][0], dp[rightchild][0], dp[rightchild][1])
# dp[node][1] = weight[node][1] + max(dp[leftchild][0], dp[leftchild][0], dp[rightchild][0], dp[rightchild][1])
# 이 과정에서 어떤 최장 노드를 구할 떄 그것이 1번 노드와 어떤 노드가 연결된 것인지 찾아야 함
# Q2를 통해 DFS 2번을 통해 찾는다는 것을 알게 되었음(왜 그런지, 어떻게 그런 사고를 도출했는지는 잘 모르겠음)
# 어쨌든 위의 과정을 1번과 최장거리에 있는 노드를 구한 후 그 노드A에 대해서 반복 처리한 후...
# A에서 최장 노드인 노드 B를 찾으며, 그때 그 최장 거리 값을 출력한다.


#🔍 Q2. 트리에서 가장 긴 거리(지름)를 효율적으로 구하는 방법은?
#📌 전략: DFS 2번
#1차 DFS: 아무 노드(보통 1번)에서 시작 → 가장 먼 노드 A를 찾는다

#2차 DFS: A에서 다시 DFS → 가장 먼 노드 B를 찾는다

#A ↔ B 거리 = 트리의 지름

#💬 왜 2번 DFS인가?
#트리는 사이클이 없으므로, A에서 B로 가는 경로는 유일하고,

#이 경로가 항상 트리 내 최장 경로가 되기 때문이야.


import sys
from collections import defaultdict
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N = int(input())
# 그래프 구성
graph = defaultdict(list)

# 양방향 간선 연결(가중치도 이용해야 하므로, 연결된 노드와 가중치를 튜플 형태로 저장)
for _ in range(N - 1):
    u, v, weight = map(int, input().split())
    graph[u].append((v, weight))
    graph[v].append((u, weight))


def dfs(node, distance):
    visited[node] = True
    for neighbor, weight in graph[node]:

        if (visited[neighbor] != True):
            dist[neighbor] = distance + weight 
            dfs(neighbor, distance + weight)
            
# 1차 DFS(1번 노드로부터 가장 먼 노드 A를 찾는 과정)
# 노드 1번 부터 ~ N번까지 배열 인덱스로 접근하기 위해서
visited = [False for _ in range(N+1)]        
dist = [0 for _ in range(N+1)]

dfs(1, 0)

A = dist.index(max(dist))

# 2차 DFS(노드 A로부터 가장 먼 노드 B를 찾는 과정, A-B 사이의 거리가 트리의 지름)
visited = [False] * (N + 1)
dist = [0] * (N + 1)

dfs(A, 0)
print(max(dist))  # 트리의 지름

