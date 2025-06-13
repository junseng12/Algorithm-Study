# ### 🚀 셀프 테스트용 문제 (Algorithm 학습용)

# #### 📌 문제명: "공항 이용 가능 여부 확인하기"

# #### 📝 문제 설명

# * N개의 공항(도시)이 있고, 일부 공항끼리는 **직항 노선**이 존재한다.
# * M개의 직항 노선 정보가 주어진다 (양방향으로 비행 가능).
# * 이후 여행 계획으로 K개의 공항을 순서 없이 제시한다.
# * 당신은 **"해당 여행 계획에서 모든 공항이 서로 비행 가능하게 연결되어 있는지"** 확인해야 한다.

# #### 🚩 입력

# * 첫 줄에 N (공항 수), M (직항 노선 수) 주어짐.
# * 이후 M줄에 두 개의 공항 번호 A, B (직항 노선 A-B 존재).
# * 다음 줄에 K (여행 계획에 포함된 공항 수).
# * 다음 줄에 K개의 공항 번호가 공백으로 구분되어 주어짐.

# #### 🚩 출력

# * **YES** → 여행 계획에 포함된 모든 공항이 같은 연결된 집합에 속한다면.
# * **NO** → 그렇지 않으면.

# #### 🚩 예시 입력

# ```
# 5 4
# 1 2
# 2 3
# 4 5
# 1 3
# 3
# 1 2 3
# ```

# #### 🚩 예시 출력

# ```
# YES
# ```

import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)


N, M = map(int, input().split())

parent = [ i for i in range(N+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root  # 또는 rank 기준으로 최적화 가능


for _ in range(M):
    u, v = map(int, input().split())
    union(u,v)

K = int(input())

# plan = [0 for _ in range(K)]   --> 필요 없음. 바로 아래 코드로 충분
plan = list(map(int, input().split()))


root = find(plan[0])


for airport in plan[1:]:
    if root != find(airport):
        print("NO")
        break
else :
    print("YES")