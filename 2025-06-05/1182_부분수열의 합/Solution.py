# Problem: 1182_부분수열의 합
# Date: 2025-06-05
# Language: Python 3

# 조건
# N 개의 정수로 이루어진 수열 존재
# 크기가 양수인 부분수열 중 그 수열의 원소를 다 더한 값이 S 가 되는 경우의 수 구하라

# 가정
# 첫째 줄 : 정수 개수 N, 정수 S (1 ≤ N ≤ 20, |S| ≤ 1,000,000)
# 둘째 줄 : N개의 정수
# 각 정수의 절댓값은 100,000 을 넘지 않음

# 아이디어 : 
# 각 인덱스를 기준으로 하나하나 씩 넘어간다고 하면..
# 첫째 인덱스가 들어가는 경우 - 이후에 다른 것들 선택하면서 합을 비교(dfs 처리)
# 둘째 인덱스가 들어가는 경우 - 
# ....

# dfs에서 저장해야 할 것들 : 지금까지 구해온 합(local 상에서 저장하여 S와 같은지?), count 변경(global 변수로 설정), 
# 특정 조합에서 S 가 되었다가, 거기서 몇 개의 숫자를 더 추가하였을 떄도 S 가 나온다면 다른 case로 고려해야 함
        
# Q1-1. "부분수열"이란 무엇이고, 이 문제에서 어떤 조건을 만족해야 할까?
# 부분적으로 일부 정수를 더하여 그 총합이 S 값을 만족해야 함

# Q1-2. 상태 변화는 어떤 식으로 정의할 수 있을까? 예: 인덱스, 현재 합
# 상태 변화는 현재 인덱스를 순차적으로 이동하며 정의한다. 각 과정에서는 현재까지의 합을 저장해가며 비교할 수 있음

# Q1-3. 재귀 탐색(DFS) 중 어떤 시점에 카운트를 증가시켜야 할까?
# 이거는 잘 모르겠다.

# Q1-4. 원소를 포함/비포함하는 선택 구조를 어떻게 표현할 수 있을까?
# visited 배열로써 표현할 수 있지 않을까 싶음

# Q1-5. S=0일 때, 아무 원소도 선택하지 않은 경우(공집합)도 포함해야 할까?
# 포함해야 해서는 안된다 크기가 양수여야 한다고 했기 때문임


import sys
from collections import defaultdict
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

# 그래프 구성
graph = defaultdict(list)

N, S = map(int, input().split())

numlist = list(map(int, input().split()))
# visited = [False for _ in range(N)]


count = 0


def dfs(idx, current_sum):
    global count
        
    if idx == N:
        if current_sum == S:
            count += 1
        return
    
    # 각 요소는 본인이 포함되는지 안 포함되는지 2가지 경우 존재
    dfs(idx + 1, current_sum + numlist[idx])  
    dfs(idx + 1, current_sum)

dfs(0, 0)

# 공집합 예외 처리
if S == 0:
    count -= 1

print(count)