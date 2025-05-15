# Problem: 9184_신나는 함수 실행
# Date: 2025-05-15
# Language: Python 3

# 조건
# 제시된 재귀함수 w(a, b, c)에 대해 이것보다 더 효율적인 방식으로 구현하여 a, b, c가 주어졌을 때, w(a, b, c)를 구하시오

# 가정
# 입력은 a, b, c 세 정수로 주어지며, 한 줄에 a, b, c 한 쌍으로 제공
# 입력의 마지막은 -1, -1, -1로 나타내며(마지막 입력을 제외하면 입력값 중 -1, -1, -1 값 없도록 함)
# -50 ≤ a, b, c ≤ 50

# 아이디어 : 
# 재귀함수 w(a, b, c)에 대한 조건 정리 후 효율적인 방안 계산
# 조건 1) a or b or c <= 0 이면 return 1
# 조건 2) a or b or c > 20 이면 return w(20, 20, 20)
# 조건 3) a < b 이고 b < c이면 return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
# 위 조건 어디에도 속하지 않는다면 return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

#🧠 Q1. 어떤 입력에서 함수는 항상 1을 반환해야 할까?
#🧩 Hint 1: 문제의 조건 중 가장 먼저 체크되는 분기 조건을 찾아보세요.
#🧩 Hint 2: 그 조건이 만족되면 왜 더 이상 재귀 호출 없이 결과가 정해질까요?
# (a <= 0) or (b <= 0) or (c <= 0) 일 때 그렇다
# 입력의 마지막을 -1, -1, -1로 나타내기로 했었는데.. -1, -1, -1 값에 대해서는 입력 처리를 마무리하도록 설정했기 때문임

#🧠 Q2. 입력이 너무 크거나 작을 때, 우리가 실제 계산할 범위를 제한하려면 어떻게 해야 할까?
#🧩 Hint 1: a, b, c가 20보다 클 경우, 함수는 어떤 인자를 넣어 다시 호출되나요?
#🧩 Hint 2: 이 조건은 왜 존재할까요? 메모이제이션 범위를 어떻게 줄일 수 있을까요?
# 입력 값의 크기가 20보다 크면 계산 범위가 커져서 줄이기 위해 여기서는 w(20,20,20)으로 재 처리하도록 하여, 계산 범위를 줄이고 있다
import sys
sys.setrecursionlimit(100000)
  
dp = [[[None for _ in range(21)] for _ in range(21)] for _ in range(21)]
  

def w(a, b, c):
  if ((a <= 0) or (b <= 0) or (c <= 0)):
    return 1
  if ((a > 20) or (b > 20) or (c > 20)):
    return w(20, 20, 20)
  # ↓↓메모이제이션을 사용하는 재귀 DP에서 반드시 필요한 줄 
  if dp[a][b][c] is not None:
    return dp[a][b][c]
    
  if ((a < b) and (b < c)):
    dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
  else: 
    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
  return dp[a][b][c]



while True :
  a, b, c = map(int, input().split())
  if((a == -1) and (b == -1) and (c == -1)):
    break
  print(f"w({a}, {b}, {c}) = {w(a,b,c)}")
