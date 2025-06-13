# Problem: 1976_여행가자
# Date: 2025-06-12
# Language: Python 3

# 조건
# 도시가 N개 있고 임의의 두 도시 사이에 길이 있을 수도, 없을 수도 있음
# 여행 일정이 주어졌을 때, 이 여행 경로가 가능한 것인지 알아보자
  # 중간에 다른 도시를 경유해서 여행을 할 수도 있음

# 도시들의 개수와 도시들 간의 연결 여부가 주어져 있고, 동혁이의 여행 계획에 속한 도시들이 순서대로 주어졌을 때, 가능여부 판별

# 가정
# 첫 줄: 도시의 수 N (N은 200이하)
# 둘째 줄: 여행 계획에 속한 도시들의 수 M(M은 1000이하)
# ~(다음 N개의 줄): N개의 정수  [i번째 줄의 j번째 수는 i번 도시와 j번 도시의 연결 정보]
# 마지막 줄: 여행 계획

# 아이디어 : 
# 간선 상의 가중치 개념 X, 최단 경로 문제 아님
# 양항뱡 그래프 문제
# visited 중복 가능

# 단순 가능한지 여부를 알려고 한다면.. 모든 경우 탐색하는 것이 일반적임 => dfs
# 

# Q1-1️⃣: 이 문제는 MST 문제인가? 아니면 어떤 문제 유형으로 보는 것이 맞는가?
# WHY 단계에 집중
# 이 문제는 MST 문제로 보지 않는다. MST는 최소 비용으로 연결된 집합 생성과 관련된 문제로 느꼈고, 현 문제는 경로의 존재 유무 문제로 dfs나 bfs 로 문제는 푸는 유형 같다


# Q1-2️⃣: Union-Find는 어떤 방식으로 활용하게 될까?
# 이번에는 MST 구성이 아니라 어떤 관점으로 사용되는지 사고해보기
# union-find 를 어떤 식으로 구성해야 하는지는 솔직히 잘 모르겠다.
# 이걸 사실 보면서, 경로 탐색 문제이긴 한데.. 매 여행 계획 도시에 도달할 때마다 해당 새로운 목표 도시에 대한 dfs로 새로 호출하여, 처리하면 도시 중복 방문 고려하지 않고도 처리 가능할 듯함

# Q1-3️⃣: 입력에서 주어지는 도시 간 연결 정보는 어떻게 처리하면 좋을까?
# 그래프를 어떤 구조로 변환할지, Union-Find 초기화는 어떻게 할지
# 2차원 배열처럼 제시되는 도시 간 연결 정보를 일단 그래프로 받는 게 다루기 용이할 것 같다고 생각했는데..
# union-Find 초기화는 잘 감이 안온다

# Q1-4️⃣: 여행 계획 검증은 어떤 흐름으로 진행해야 할까?
# Union-Find로 무엇을 확인하면 되는지
# 아직 모르겠다

# 종료 조건
# 여행 경로 배열 = [A, C, B, C]
# 하나씩 빼서 찾다가... 해당 배열의 크기가 0일 때. 더 뺄 게 없을 떄 종료

import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root  # 또는 rank 기준으로 최적화 가능


N = int(input())
M = int(input())

connected = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
  connected[i] = list(map(int, input().split()))


parent = [i for i in range(N+1)]   # Union-Find parent 리스트(초기에는 자기 자신이 부모)

for i in range(N):
  for j in range(N):
    # 그 후 인접 행렬 읽으며:
    if connected[i][j] == 1:
        union(i+1, j+1)  # 문제에서 도시는 1-based index임
      
# 여행 계획
plan = list(map(int, input().split()))

# 기준 도시
root = find(plan[0])

# 나머지 도시들도 모두 같은 root인지 확인
for city in plan[1:]:
    if find(city) != root:
        print("NO")
        break
else:
    print("YES")

