# Problem: 9663_N-Queen
# Date: 2025-06-06
# Language: Python 3

# 조건
# 크기가 N × N인 체스판 위, 퀸 N개를 서로 공격할 수 없게 놓는 문제
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하라

# 가정
# 첫째 줄: N (1 ≤ N < 15)

# 아이디어 : 
# 퀸의 이동 범위 (가로, 세로, 대각선 전부)
# 퀸 N 개를 서로 공격할 수 없도록 만드려면 해당 이동 범위 겹치지 않아야 함
# 퀸 1개를 놓았을 때, 다음 번에 퀸 N-1 개의 위치를 고려할 때는 퀸 1개의 위치에 따라 고려 범위가 달라짐
# 퀸 1개 놓으면, 가로 N 개, 세로 N개, 대각선 N개 (물론, 겹치는 범위로 인해 실제 N-1, N-1, N-1, 퀸 놓은 위치 1개 이렇게 사용 불가)

# 2차원 visited_col 배열을 생성하고, 퀸 1개를 놓을 때(i, j)마다 visited_col 배열 변경(false -> True)
# visited_col[i][] = True, visited_col[][j] = True

# 문제는 대각선을 어떻게 처리하느냐... 인데.
# 0 <= i, j <= N 범위 내일 때에 대해서만 계속 반복하여 1) visited_col[i-1][j-1], 2) visited_col[i+1][j+1], 3) visited_col[i-1][j+1], 4) visited_col[i+1][j-1] 
# 이렇게 처리하면 될 것 같긴 함 ->> 너무 노가다 적인데?

# 사실 상 문제가 체스판 N X N 이기 때문에, N개의 퀸을 두려면 한 줄(행, 열 따로따로 관점에서)에는 무조건 퀸 하나가 놓여져야 함
# 그러면, 그냥 임의로 설정해보자고 첫 퀸은 무조건 첫 행에 두고, 두 번째 퀸은 무조건 두번쨰 행에 두고 하는 식으로
# 여기서는 열의 위치를 어떻게 선정하느냐 에 따라 여러 경우가 나오겠지만..
# 그러면, 실질적으로 dfs 처리 마다 증가하는 것은 row이고, 이를 이전 depth 처럼 처리할 수 있음

# 아예 가로 세로는 다음과 같이
# visited_col[i][] = True, visited_col[][j] = True
# 이렇게 각 퀸을 놓을 때(i,j)마다 처리하여 확인할 수 있도록 한다지만..(놓을 떄마다 퀸 queen +=1 )


# 다만, 대각선이 어떻게 겹치지 않도록 하느냐...
# 위에서 아래로 내려가며 처리하니까.. 0 <= i, j <= N 범위 내일 때에 대해서만 계속 반복하여 1) visited_col[i+1][j+1], 2) visited_col[i+1][j-1] 이 두 부분들을 확인해서 visited_col = True 처리해주면 
# visited_col !=  True 이걸로 필터링할 수 있지 않을까?

# =>> ⚠️ 2차원 visited_col 배열로 대각선을 처리하는 방식 — 너무 비효율적이다
# 이유:
# 대각선은 좌표 간 연산으로 간단히 표현 가능하다. 일일이 visited_col[i ± k][j ± k]를 하는 건 시간복잡도가 너무 높고, 구현도 복잡해진다.

# 💡 핵심 아이디어:
# ↙ 대각선 (우상 → 좌하): 모든 좌표 (i, j)에서 i + j 값이 같음
# i 값은 증가하는데, j 값은 감소하여서
# ↘ 대각선 (좌상 → 우하): 모든 좌표 (i, j)에서 i - j 값이 같음
# i 값도 증가하고, j 값도 증가하여서

# diag1[i - j + (N - 1)]  # ↘ 좌상 → 우하
# diag2[i + j]            # ↗ 우상 → 좌하


# 기저 조건
# queen == N일 때.. 종료 및 해당 경우의 수 기록 (count +=1)
# 아무데도 놓을 수 있는 경우가 없을 때, 종료
    # 놓을 수 있을 때와 놓을 수 없을 떄 어떻게 조건 분기로 처리?
    # visited_col 배열의 열을 돌면서... 
      
# dfs 처리 과정에서 어떤 매개변수를 추가로 넣어 전달해야 하나?
# 이전까지 놓은 퀸의 개수 +1 하여 넣기
# count는 전역 변수로 처리


# 백트래킹
# visited_col[i][] = True, visited_col[][j] = True
# dfs(row+1, queen + 1)
# visited_col[i][] = False, visited_col[][j] = False

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)


N = int(input())

visited_col =[False for col in range(N)]

diag1 =[False for col in range(2*(N-1)+1)]
diag2 =[False for col in range(2*(N-1)+1)]

count = 0

def dfs(row):
    global count
    
    # Queen을 다 놓아서 놓을 필요 없는 경우
    # row 의 깊이 == 놓은 Queen의 개수
    if row == N:
        count += 1
        return
  
    for col in range(N):
        # Queen을 놓을 수 있는 경우 
        # visited_col 배열을 2차원으로 사용하려고 했음 --> 실제로는 가로(행)는 row 기준으로 고정하므로(계속 증가시켜 안 겹치도록 하니까..), 세로(열)는 col 기준으로 탐색하므로 col만 체크하면 됨.
        if (visited_col[col] != True) and (diag1[row - col + (N - 1)] != True) and (diag2[row + col] != True):
            
            visited_col[col] = True
            diag1[row - col + (N - 1)] = True
            diag2[row + col] = True
            dfs(row+1)
            visited_col[col] = False
            diag1[row - col + (N - 1)] = False
            diag2[row + col] = False
        
    

dfs(0)

print(count)