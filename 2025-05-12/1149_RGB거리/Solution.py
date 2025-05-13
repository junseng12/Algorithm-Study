# Problem: 1149_RGB거리
# Date: 2024-05-12
# Language: Python 3

# 조건
#집이 N개 존재, 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있음
#집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 함
#각 색깔마다 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하며 모든 집 칠하는 비용 최솟값 구함

# 가정
# 규칙 3가지
# 1) 1번 집의 색은 2번 집의 색과 같이 않아야 함
# 2) N번 집의 색은 N-1번 집의 색과 같이 않아야 함
# 3) i(2<=i<=1000)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 함

# 첫째 줄 입력 :  N(2 ≤ N ≤ 1,000)
# 둘째 줄 ~ N번째 줄 입력 : 각 집을 빨강, 초록, 파랑으로 칠하는 비용 (한 줄에 하나씩(R,G,B 비용))

# 아이디어 : 
# dp(i) - i번째 집까지 칠한 최소 비용 -> 2차원 배열 idea
# R[i], G[i], B[i] - i번째의 집에 칠하는 각 색깔 별 비용 배열 => 2차월 배열로 선택한다면..?
# dp[i][] = min(dp[i-1][R] + cost[i][G], dp[i-1][R] + cost[i][B], dp[i-1][G] + cost[i][R], dp[i-1][G] + cost[i][B], dp[i-1][B] + cost[i][R], dp[i-1][B] + cost[i][G])
# 근데 이건 너무 많은데..?
# dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + cost[i][R]
# dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + cost[i][G]
# dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + cost[i][B]


#❓ Q1. 어떤 상태를 DP로 정의할 수 있을까?
#dp[i][c] = ??? ← 이걸 어떻게 정의할 수 있을까?
#i 번째 집까지의 최소 색칠 비용이며, i번째에는 c 색으로 칠함


#❓ Q2. 색이 3가지(R, G, B)일 때,
#→ i번째 집을 어떤 색으로 칠할 때, 바로 전(i-1) 집의 색은 어떻게 제한될까?
# i번쨰 집을 R 이라고 칠한다고 한다면.. i-1에 대해서는 G, B로 결국 2개의 선택지로 제한됨

N = int(input())

# cost = [[0 for j in range(3)] for i in range(N)]

# for i in range(N):
#   R, G, B = map(int, input().split())
#   cost[i][0] = R
#   cost[i][1] = G
#   cost[i][2] = B
# >>> 더 간단하게 나타낸 표현 >>>
cost = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for j in range(3)] for i in range(N)]
dp[0][0] = cost[0][0] #cost[0][R]
dp[0][1] = cost[0][1] #cost[0][G]
dp[0][2] = cost[0][2] #cost[0][B]


for i in range(1, N):
  dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0] #dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + cost[i][R]
  dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1] #dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + cost[i][G]
  dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2] #dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + cost[i][B]  
  
print(min(dp[N-1]))