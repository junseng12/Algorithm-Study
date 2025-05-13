# Problem: 1005_ACM_Craft
# Date: 2024-05-07
# Language: Python 3

# 조건
#건물을 짓는 순서가 정해져 있지 않음 -> 즉, 첫 번째 게임과 두 번째 게임이 건물을 짓는 순서가 다를 수도 있다.
# 매 게임시작 시 건물을 짓는 순서가 주어진다.
# 모든 건물은 각각 건설을 시작하여 완성이 될 때까지 Delay 존재
# 특정건물을 가장 빨리 지을 때까지 걸리는 최소시간을 알아내자

# 가정
# 맨 첫째 줄: 테스트케이스의 개수 T 입력
# 테스트 첫 줄: 건물의 개수 N, 건물간의 건설순서 규칙의 총 개수 K이 주어짐
# 테스트 두번째 줄 : 각 건물당 건설에 걸리는 시간 D1, D2, ..., DN이 공백을 사이로 주어짐
# 테스트 세번째 줄 : 셋째 줄부터 K+2줄까지 건설순서 X Y 주어짐(건물 X를 지은 다음에 건물 Y를 짓는 것이 가능하다는 의미)

#2 ≤ N ≤ 1000
#1 ≤ K ≤ 100,000
#1 ≤ X, Y, W ≤ N
#0 ≤ Di ≤ 100,000, Di는 정수



# 아이디어 : 
#❓ Q1. 건물 간 선후 관계를 어떤 자료 구조로 표현하면 좋을까?
# 특정 노드 A를 건설하는데 걸리는 시간 D A 값, 건설 순서 A B(A->B순으로 건설)값을 가지고 있는 링크트 리스트로 표현하면 편리할 수 있을 것 같다. 

#❓ Q2. 특정 건물을 짓기 위해 먼저 어떤 건물이 끝나야 할까? → 최대 몇 초가 걸릴까? 라는 계산 방식은?
# 가장 처음 접근하는 노드의 경우에는 일단 D1 값을 총 걸리는 시간에 더하고, 
# 이후에는 건설 순서에 포함된 건물 건설 시간이 여러 개일 경우, (그러니까 A에 A B, A C, A D이렇게 노드 A가 가지고 있을 경우) 그것을 타고 넘어간 각 노드 B, C, D의 건설 시간 중 최댓값을 반영한다.

#❓ Q3. DP[i]를 "건물 i를 완성하는 데 걸리는 최소 시간"이라 한다면, → 어떤 점화식을 세울 수 있을까?
# DP[i] = DP[i - 1] + max(NodeA.건설순서 A B -> 건설 시간, NodeA.건설순서 A C -> 건설 시간, ...) 
# (보니까 한 노드당 건설 순서 X Y 를 가질 수 있는 개수가 다를 것 같아, for in range 반복문으로 첫 값 변수에 저장해놓고 계속해서 최댓값 업데이트 하는 방식 하면 되지 않을까 싶음)

from collections import deque
import sys
input = sys.stdin.readline

T = int(input()) #테스트 케이스의 개수 T

for _ in range(T):
  N, K = map(int, input().split()) # 건물의 개수 N, 건물간의 건설순서 규칙의 총 개수 K

  adj = [[] for _ in range(N + 1)]       # 인접 리스트: A → B
  indegree = [0] * (N + 1)               # 각 노드의 진입 차수
  time = [0] * (N + 1)                   # 각 건물의 고유 건설 시간
  dp = [0] * (N + 1)                     # 건물 완성까지 걸리는 누적 시간

  inputs = list(map(int, input().split())) # 입력받은 각 건물의 고유 건설 시간
  start_index = 1 #인덱스 1 부터 각 건물 요소(진입차수, 건설 시간) 고려         
  for i, val in enumerate(inputs):
      time[start_index + i] = val
      
  for _ in range(K):
    X, Y = map(int, input().split())
    adj[X].append(Y)
    indegree[Y] += 1
    
  W = int(input())  # 게임에서 승리하기 위해 건설해야 하는 특정 건물
  
  # 위상 정렬 준비
  queue = deque()
  
  for i in range(1, N+1):
    if (indegree[i] == 0):
      queue.append(i)
      dp[i] = time[i]
      
  #dp[i]: 건물 i를 짓기 위해 필요한 모든 선행 건물들이 끝나고, → 그 다음에 건물 i를 시작한다고 할 때의 최종 완성 시간
  while queue:
    cur = queue.popleft()
    
    for next in adj[cur]:
      dp[next] = max(dp[next], dp[cur] + time[next])
      indegree[next] -= 1
      
      if(indegree[next] == 0):
        queue.append(next)
    
        
  print(dp[W])

  