# Problem: 12851_숨바꼭질 2
# Date: 2025-05-17-18
# Language: Python 3

# 조건
# 숨바꼭질 게임 (수빈이 : 현재 점 N, 동생 : 점 K)
# 수빈이는 걷거나 순간이동 가능
# 수빈이의 위치가 X일 때, 
# 1) 걷는다면 1초 후에 X-1 or X+1로 이동
# 2) 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지?, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지? 구하는 프로그램

# 가정
# 첫째 줄 : 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어짐
# N과 K는 정수 (0 ≤ N ≤ 100,000), (0 ≤ K ≤ 100,000)

# 아이디어 : 
#🧠 Q1. 최단 거리 탐색과 경우의 수 계산을 동시에 하려면 어떤 구조를 설계해야 할까?
#💡 Hint 1: BFS는 최단 거리 탐색에 특화되어 있습니다.
#하지만 최단 거리 경로가 여러 개 있을 경우, 이들을 어떻게 누적할지 설계가 필요합니다.

#💡 Hint 2: visited 배열은 단순 방문 여부(True/False)만으로는 부족합니다.
#무엇을 저장해야 경로의 "시간"과 "수"를 모두 추적할 수 있을까요?

# 최단 거리 탐색과 경우의 수 계산을 동시에 처리하려면 1차원 배열로는 불가능함 
# 따라서 2차원 배열로 설정하여 문제 진행함 dp[i][j] 
# 최단 경로가 여러 개 있다면... dp[i][j] : i에서 j로 가는 가장 빠른 시간 이라 했을 떄
# 새로운 배열 하나를 선언하여 visited[i][j]라 하고, 이것은 i에서 j로 갈 때 가는 경우의 수 로 생각하면 되지 않을까?
# 솔직히 잘 감이 안 온다..

# visited[i] : i번째 위치까지 도달한 최소 시간 저장
# count[i] : i번째 위치에 도달한 총 경우의 수

#🧠 Q3. visited[next] > visited[now] + 1 대신
#혹시 visited[next] >= visited[now] + 1을 쓰면 왜 틀릴까?
# BFS 개념상 현재 레벨에서의 시간은 무조건적으로 다음 레벨에서의 시간보다 크다. ( visited[now] < visited[next])
# 해당 진행 경로가 최단 경로인 경우라도 now에서 i를 찾지 못했다면, next로 넘어가게 되겠지?
# 근데.. visited[next] = visited[now] + 1이면, now 내 배열 요소 중 하나에서 해당 특정 경로로 가는 것만을 고려한다는 느낌이 듦(정확하지는 않음)
# visited는 BFS이기 때문에... 배열 내 모든 요소에서 각 레벨에 맞는 모든 경우의 수를 구하여야 하고, 이를 통해 최단 거리 내 i 로의 최단 시간을 보장하므로 = 이 포함되서는 안됨.. 맞나..?
from collections import deque

N, K = map(int, input().split())
MAX = 100001

visited = [float('inf')] * MAX  # 최소 시간 저장
count = [0] * MAX               # 경우의 수 저장

queue = deque()

queue.append(N)
visited[N] = 0
count[N] = 1



while queue :
  now = queue.popleft()
  
  for next in [now -1, now +1, 2* now] :
    if (0 <= next < MAX):
      if (visited[next] > visited[now] + 1):
        # 더 빠른 경로 발견 → 정보 초기화
        visited[next] = visited[now] + 1
        count[next] = count[now]
        queue.append(next)
      elif (visited[next] == visited[now] + 1):
        # 같은 시간에 또 다른 경로 발견 → 경로 누적
        count[next] += count[now]
        
print(visited[K])
print(count[K])
        