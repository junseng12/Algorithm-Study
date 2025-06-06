# Problem: 15649_N과 M (1)
# Date: 2025-06-05
# Language: Python 3

# 조건
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하라
# ) 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

# 가정
# 첫째 줄: 자연수 N, M (1 ≤ M ≤ N ≤ 8)

## 출력
# 한 줄에 하나씩, 문제의 조건을 만족하는 수열 출력
# 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력
# 사전 순으로 증가하는 순서로 출력

# 아이디어 : 
# 수학에서 nPm, 조합 개념을 이용하는 개념인 것 같다
# 여기에서는 범위 M~N 내 속하는 정수들에 대해서 m 만큼 선택하는 모든 경우의 수에 대해 그 각 경우의 수를 한줄에 하나씩 출력하여 모두 출력하는 것
# 1) 1~N 범위 내 숫자 리스트를 생성
# 2) 이 리스트 내에서 M 개의 숫자를 선택하는 경우의 수를 연산
# 3) 각 연산한 내용을 저장하고 한 줄에 한 경우 씩 모두 출력함

# dfs 관점에서 처리하려면
# 각 숫자들은 선택하거나 선택하지 않거나, 2가지 경우 존재함
# 각 숫자들을 선택하는 경우라면 전체 길이가 M이니까 M 의 길이 를 기억하여 하나를 줄여서 적용해야 함
# 선택한 경우에는 특히, 선택한 애들을 같이 전달해 줘야 기억함

# 선택하지 않는다면, 인덱스만 증가시켜서 dfs 처리 이어서 하면 될 듯

# dfs 가 저장해야 하는 것
# 선택한 요소
# index

# 기저 조건
# 각 숫자 포함된 것이 M에 도달했을 경우
# 모든 리스트 요소에 대해 선택 처리했을 경우



# 🧩 사고 개선 흐름 예시
# ❓질문: 숫자를 고를 때 '선택할지 말지'가 아니라면, 뭘 기준으로 고르지?

# → ✅ “아직 고르지 않은 숫자 중 하나를 고르자”
# → ✅ 그래서 필요한 것이 used 배열이다
# → ✅ 매 DFS 호출마다 for i in range(1, N+1) 을 돌면서
# → ✅ 아직 사용하지 않은 i를 append하고, used[i]=True 후 재귀
# → ✅ 그 후에는 반드시 pop + used[i]=False 해서 원상 복구



import sys
from collections import defaultdict
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

seq = []

for i in range(1, N + 1):
    seq.append(i)



used =[False for _ in range(N+1)]

    
    
def dfs(depth, path):
    if depth == M:
        print(' '.join(map(str, path)))
        return
    
    for i in range(1, N+1):
        if used[i] != True:
            path.append(i)
            used[i] = True
            dfs(depth + 1, path)
            path.pop()
            used[i] = False
            
            
dfs(0, [])