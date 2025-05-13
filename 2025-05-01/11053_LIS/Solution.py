# Problem: 11053 LIS
# Date: 2024-05-01
# Language: Python 3

# 조건
#수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열의 길이를 구하라.
#예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

#첫째 줄에 수열 A의 크기 N 입력 (1 ≤ N ≤ 1,000)
#둘째 줄에는 수열 A를 이루고 있는 Ai 입력 (1 ≤ Ai ≤ 1,000)

# 가정
# dp[i] = A[i]를 [마지막 원소]로 가지는 가장 긴 증가 부분 수열의 길이 -> 순방향적 시도가 유리함 

# 아이디어 : 
# 순방향적 시도에 따른 점화식 설계 : dp[i] = max(dp[j] + 1) j < i이고 A[j] < A[i]
# dp[j]에서부터 해왔던 연산보다 dp[i]부터 시작하는 연산이 더 클 수 있음을 고려하여(연산이 끊기는 경우), 다시 점화식 보충 설계 : dp[i] = max(dp[i], dp[j] + 1) j < i이고 A[j] < A[i]

N  = int(input())

A = [None for i in range(N)]
A = list(map(int, input().split()))

# 초기 조건 설정 (1 ≤ Ai ≤ 1,000)이므로 dp[i]의 모든 원소에 대해 1로 초기화
dp = [1 for _ in range(N)]

for i in range(N):
  for j in range(i):
    if (A[j] < A[i]):
      dp[i] = max(dp[i], dp[j] + 1)
      
      
print(max(dp))

