# Problem: 16987_계란으로 계란치기
# Date: 2025-06-01
# Language: Python 3

# 조건
# 계란으로 계란 치기 활동
# 각 계란에는 내구도, 무게 존재
# 계란으로 계란을 침 -> 각 계란의 내구도 = 각 계란의 내구도 - 상대 계란 무게 
# 내구도 0이하 되는 순간, 계란 깨짐
# 일렬로 놓여있는 계란 에 대해, 왼쪽부터 차례로 들어서 한 번씩만 다른 계란을 쳐 최대한 많은 계란을 깨는 문제

# 과정
# 1) 가장 왼쪽의 계란을 든다
# 2) 손에 들고 있는 계란으로 꺠지지 않은 다른 계란 중에서 하나를 침
#   단, 손에 든 계란이 꺠졌거나 꺠지지 않는 다른 계란이 없으면 치지 않고 넘어감
# 3) 가장 최근에 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 과정 다시 진행
#   단, 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 계란 치는 과정 종료함

## 목표 : 최대한 많은 계란을 깨는 것

# 가정
# 첫째 줄: 계란의 수 N(1 ≤ N ≤ 8)
# 두번째 ~ (N개의 줄): 각 계란의 내구도 Si(1 ≤ Si ≤ 300)와 무게 Wi(1 ≤ Wi ≤ 300)

# 출력 :  깰 수 있는 계란의 최대 개수

# 아이디어 : 
# 일단 각 계란에 대해 일렬로 구성되어 있으므로, 배열에 순서대로 각 계란의 내구도 Si, 무게 Wi 구성(2차원 배열) >>> 명시적으로 하기 위해 Si와 Wi 를 분리
# dp[i][0] = 내구도, dp[i][1] = 무게..
# 첫 시작점은 항상 왼쪽 끝 계란
# 최대로 많이 깨려면... 결국 무게 높은 것을 이용하여 많이 때려야 하지 않나..? 그리고 그것의 내구도를 최대한 활용해야 함
# 

# ✅ 실습 전 구조적 질문 (Q1 단계)
# Q1-1. 각 계란의 상태는 어떤 정보로 표현될 수 있을까?
    # 2차원 배열로 표현하면 되지 않을까 싶었음.
# Q1-2. 한 계란이 다른 계란을 칠 때, 어떤 조건을 만족해야 공격이 가능한가?
    # 한 계란과 다른 계란이 내구도가 0이하가 아닌 경우( 그러니까, 둘 다 깨지지 않은 경우)
# Q1-3. DFS가 탐색해야 할 상태는 무엇이 바뀔 때마다 달라지나?
    # 매 차례에 각 계란의 내구도의 변화를 보고 만약 0 이하의 내구도를 가진 계란의 수의 변화가 생긴다면.. DFS 탐색해야 할 상태가 달라지지 않나? 
# Q1-4. 탐색의 종료 조건은 어떤 상황일까?
    # 결국 맨 오른쪽 계란을 드는 차례가 되었을 때..
# Q1-5. DFS 탐색 과정에서 원상 복귀(백트래킹)를 왜, 어디서 해야 할까?
    # DFS 탐색 과정에서 백트래킹을 해야 하는 이유는 내가 생각하기에, 어떤 계란을 치는지에 따라 최종 결과가 달라지니까... 그것에 따른 각 경우를 독립적으로 확인하기 위해 백트래킹이 필요함.
    # 어느 지점에서라고 한다면.. 각 계란을 치는 순서를 depth라고 하자. 그럼 맨왼쪽에서부터 총 N까지의 depth가 존재할 것임
    # 그렇다면, 각 지점에서 바로 전 depth로 돌아가며, 각 내구도 변화를 돌려놓는 것이 옳다. (만약, N depth까지 처리하면 일부 백트래킹하여 N-1 depth로 돌아가 다른 선택을 했을 때의 최종 깰 수 있는 계란의 개수 max 값 업데이트?)
          
import sys
from collections import defaultdict
input = sys.stdin.readline

# 1. 재귀 깊이는 여유 있게 10000 정도로만 설정
sys.setrecursionlimit(10000)

# 그래프 구성
graph = defaultdict(list)

N = int(input())

durability = [0 for _ in range(N)]
weight = [0 for _ in range(N)]

for i in range(N):
    S, W = map(int, input().split())
    durability[i] = S
    weight[i] = W
    


count = 0

def update_answer():
    global count
    
    tmp_count = 0
    for i in range(N):
        if durability[i] <= 0:
            tmp_count += 1
    
    if tmp_count > count:
        count = tmp_count    



def dfs(idx):
    # 현재 차례가 맨 오른쪽 계란을 들 차례인 경우
    if idx == N:
        update_answer()
        return

    # 현재 들어야 하는 계란의 내구도가 0 이하인 경우
    if durability[idx] <= 0:
        dfs(idx + 1)
        return
    
      
    has_hit = False

    # 현재 들어야 하는 계란의 내구도가 0보다 큰 경우
    for j in range(N):
        # 현재 들고 있는 계란의 내구도가 0보다 크고, 칠 수 있는 계란(자기 자신이 아니며, 내구도가 0 보다 큰 계란) 이 있는 경우
        if j != idx and durability[j] > 0:
            has_hit = True
            
            # 타격 + 백트래킹
            durability[idx] -= weight[j]
            durability[j] -= weight[idx]
            dfs(idx + 1)
            durability[idx] += weight[j]
            durability[j] += weight[idx]
        
    # 현재 들고 있는 계란의 내구도가 0보다 크지만, 칠 수 있는 계란이 없는 경우(루프를 돌면서 모든 계란 확인했는데도 없음) (나머지 계란들이 다 깨진 상태)
    if not has_hit:
        dfs(idx + 1)
            
            
dfs(0)

print(count)