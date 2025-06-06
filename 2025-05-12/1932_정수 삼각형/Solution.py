# Problem: 1932_정수 삼각형
# Date: 2024-05-12
# Language: Python 3

# 조건
# 크기가 N인 정수로 이루어진 삼각형을 제시해줌
# 맨 위층부터 시작하여 아래의 수 중 하나를 선택하여 내려올 때, 지금까지 선택된 수의 최대합을 구하라
# 현재 선택한 수의 대각선 왼쪽 or 대각선 오른쪽 것만 선택 가능

# 가정
# 1<= 삼각형의 크기 N <=500
# 삼각형을 이루는 수는 모두 정수이고, 각 정수 범위(0<= 정수 <=9999)

# 아이디어 : 
# 2차원 dp로 설정해야 됨(이전 선택의 결과가 다음 선택의 제한)  
# 인덱스가 k인 정수를 선택하면 다음 선택 가능 : k or k+1 인덱스의 정수
# dp[i][k] = max(dp[i-1][k], dp[i-1][k + 1]) + cost[i][k]
# dp[i][k+1] = max(dp[i-1][k+1], dp[i-1][k + 2]) + cost[i][k+1]
# k범위가 유동적으로 바뀌는 듯함.. (for 반복문을 이중으로 구성하여 k 고려할 범위만큼 처리하면 되지 않을까?)

#❓ Q1. 각 위치에서 무엇을 저장해야 할까?
#예: dp[i][j] = ???
#위에서부터 -> 내려오는 방향으로 층을 센다고 하면 i 번째 층에서 j번째 인덱스를 선택하여 구할 수 있는 최대합을 저장해야 한다고 생각했음

#❓ Q2. dp[i][j]를 구할 때 어떤 경로에서 올 수 있을까?
#dp[i-1][j-1] 또는 dp[i-1][j] → 각각 왼쪽 위, 오른쪽 위에서 내려오는 경우
# 왼쪽 위에서 내려오는 경우
# dp[i][j] = dp[i-1][j-1] + cost[i][j]

# 오른쪽 위에서 내려오는 경우
# dp[i][j] = dp[i-1][j] + cost[i][j]

# 결론
# dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + cost[i][j]

#❓ Q3. 테두리(삼각형 가장자리)는 어떻게 처리해야 할까?
#테두리 앞쪽은 각각 오른쪽 위에서만 받도록 하고, 테두리 뒷쪽에는 왼쪽 위에서만 받도록한다


N = int(input())

cost = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * len(row) for row in cost]
dp[0][0] = cost[0][0]

for i in range(1, N):
  for j in range(i+1):
    if(j == 0):
      dp[i][j] = dp[i-1][j] + cost[i][j]
    elif((j == (len(cost[i]) - 1))):
      dp[i][j] = dp[i-1][j-1] + cost[i][j]
    else:
      dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + cost[i][j]


print(max(dp[N-1]))