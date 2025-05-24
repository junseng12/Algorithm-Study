# Problem: 1949_우수 마을
# Date: 2025-05-23
# Language: Python 3

# 조건
# G(V, E)에서 정점의 부분 집합 S에 속한 모든 정점쌍이 서로 인접하지 않으면 (정점쌍을 잇는 간선이 없으면) S를 독립 집합(independent set)이라고 함
# 독립 집합의 크기 : (정점에 가중치가 주어져 있지 않을 경우) 독립 집합에 속한 정점의 수
# (정점에 가중치가 주어져 있는 경우) 독립 집합에 속한 정점의 가중치의 합
# 독립 집합이 공집합일 때 그 크기는 0이라고 하자. 
# 최대 독립 집합: 크기가 최대인 독립 집합 
# 트리(연결되어 있고 사이클이 없는 그래프)와 각 정점의 가중치가 양의 정수로 주어져 있을 때, 최대 독립 집합을 구하라

# 가정
# 첫째 줄: 트리의 정점의 수 n (n은 10,000이하인 양의 정수)
#  1부터 n사이의 정수가 트리의 정점이라고 가정
# 둘째 줄: n개의 정수 w1, w2, ..., wn이 주어짐 (wi: 정점 i의 가중치(1 ≤ i ≤ n), 가중치들의 값은 10,000을 넘지 않는 자연수)
# 셋째 줄~ 마지막 줄: 간선의 리스트(한 줄에 하나의 간선)

# 아이디어 : 
# (i, j) 쌍을 입력받았을 때, 각 (i, j) 쌍을 비교하면서 직접적으로 연결되지 않은 Vertex의 집합을 구함(독립 집합)
# 해당 집합에 따른 Vertex 별 가중치(wi) 도 합하여 최대 독립 집합 선정해야 함

# 각 vertes 집합을 구한 다음에, 최대 독립 집합에 대한 합을 구하면서 동시에 해당 독립 집합의 구성 요소도 구해야함.
# 2가지 조건 충족 >> 2차원 배열 활용
# 밑에 고민해보니까 일반적인 dp[i][j] 형태로는 나타낼 수 없을 것 같음..
# 따라서 2가지 조건을 표현하긴 하는데.. 그 뭐야 

# 독립 집합을 구성할 때, 특정 하나 노드를 선택하게 되면, 그것과 직접 인접한 노드는 선택할 수 없음..
# 따라서 하나 노드가 독립집합에 포함되는지 아닌지 선정하면, 그것에 따른 다른 노드 선택 요소도 제한될 것임
# 이전 우수 마을 실습에서 dp[node][0], dp[node][1]일 때의 상황과 유사하지 않나 싶음

# dp[node][i] : 해당 노드에 대한 선택 유무에 따른 가중치
# dp[node][0] => 해당 노드를 독립 집합으로 선정하지 않는 경우 
# dp[node][1] => 해당 노드를 독립 집합으로 선정하는 경우
# 이렇게 정의하면..
# dp[node][0] += max(dp[child][0], dp[child][1])
# dp[node][1] += dp[child][0]

# 물론, 명확하게 정의하지는 못하겠으나 우수 마을처럼 dfs 접근이 필요할 것 같다고 느낌
# 다만, 이제 각 독립 집합 S에 대해 어떻게 구성되어 있는지를 기록해야 함.
# 독립 집합 S 내 구성 요소 저장하기 위한 구조체 선언
# 어떻게? 넣느냐 .. 그리고 어떻게 최대 독립 집합에 대한 구성요소를 식별해서 끌어오느냐?
# dp와 유사한 구조체 S , S = [[0, 0] for _ in range(N + 1)]를 선언하여
# dp의 각 경우에 따른 node 및 child append 작업을 처리하면 알 수 있지 않을까? 싶음




#🔍 Q1. 이 문제의 핵심 제약 조건은 무엇인가?
#그래프는 사이클이 없는 트리 (즉, 무방향 & 연결 & N-1개의 간선)

#각 노드는 가중치(독립 집합에 포함될 경우 얻는 이익)를 가짐

#한 노드가 독립 집합에 포함되면 인접 노드는 포함할 수 없음

#→ 어떤 유형이 떠오르니?
#이건 사실상 "부분집합 최대 이익 선택" 문제인데,
#트리 구조로 인해 DFS 순회를 하며 점화식을 구성해야 해.

import sys
from collections import defaultdict
input = sys.stdin.readline


N = int(input())
# 그래프 구성
graph = defaultdict(list)

# 인덱스에 맞추어 노드 배열(앞에 쓰레기값 하나 포함)
Weight = list(map(int, input().split()))
Weight.insert(0, -1)

# 양방향 간선 연결 (트리이므로 방향 없음)
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 0] for _ in range(N + 1)]

# 집합 자료형 선언 (독립 집합 S 내 구성 요소 저장하기 위한 구조체)
S = [[[], []] for _ in range(N + 1)]



def dfs(node, parent):
    dp[node][0] = 0
    
    dp[node][1] = Weight[node]
    S[node][1] = [node]
    
    for child in graph[node]:
        if child == parent:
            continue
        dfs(child, node)
        
        # 선택 안 한 경우: 자식 중 더 큰 쪽 선택
        # dp[child][0]와 dp[child][1] 같을 경우는 없을 것이라 생각함
        if dp[child][0] > dp[child][1]:
          dp[node][0] += dp[child][0]
          S[node][0].extend(S[child][0])
        else:
          dp[node][0] += dp[child][1]
          S[node][0].extend(S[child][1])
        
        # 선택한 경우: 자식은 무조건 제외
        dp[node][1] += dp[child][0]
        S[node][1].extend(S[child][0])
        
#노드 1을 루트 노드로 지정하여 dfs 실시(어느 점을 잡아도 상관없으나, 일반적으로 첫 노드 설정하니..)
dfs(1, -1)

print(max(dp[1][0], dp[1][1]))

if (dp[1][0] > dp[1][1]):
  print(" ".join(map(str, sorted(S[1][0]))))
else :
  print(" ".join(map(str, sorted(S[1][1]))))