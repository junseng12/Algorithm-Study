# Problem: 1068_트리
# Date: 2025-05-27
# Language: Python 3

# 조건
# 리프 노드: 자식의 개수가 0인 노드
# 트리가 주어졌을 때, 노드 하나를 지움 -> 그 때, 남은 트리에서 리프 노드의 개수를 구하라
# 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거됨

# 가정
# 첫 줄 : 트리의 노드의 개수 N (N <= 50)
# 둘째 줄: (0번 노드부터 N-1번 노드까지의) 각 노드에 대한 부모 노드
# 만약 부모가 없다면 (루트) -1이 주어짐
# 셋째 줄: 지울 노드의 번호

# 아이디어 : 
# 트리 구조
# 각 노드에 대한 부모 노드 제시해줌
# 각 노드는 부모 노드에 대한 정보 기억해야 함
# leaf 노드를 찾는 방법 - 트리 내 제거되지 않은 모든 노드에 대해 dfs 통해 parent노드로 저장되지 않은 노드 발견할 때마다 카운트함

# 특정 노드 제거 방식
# - 특정 노드 인덱스에 저장된 부모 노드 제거
# - 특정 노드를 부모로 두고 있는 노드의 인덱스에 저장된 부모 노드(=특정 노드) 제거
# - ...dfs 처리하면서 또 그 노드를 부모로 두고 있는 ...

# ### 🔍 Q2. **DFS는 어떻게 사용되는가?**

# - 그래프를 **자식 중심**으로 구성한다 (`tree[parent].append(child)`)
# - DFS를 통해 삭제된 노드를 제외하고 탐색 진행
# - **리프 노드란?** → 현재 노드의 자식이 모두 삭제되었거나 없는 경우

# ```python
# def dfs(node):
#     if not tree[node]:  # 자식이 없다면 리프
#         count += 1
#         return
#     for child in tree[node]:
#         if child != deleted:
#             dfs(child)


import sys
from collections import defaultdict
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

# 그래프 구성
graph = defaultdict(list)

N = int(input())

#각 노드의 부모 노드를 기억하고 있는 리스트
parent = list(map(int, input().split()))

# 이전 그래프 연결에서는 양방향 연걸 (하지만, 일반적인 트리에서는 부모 -> 자식 단방향 구조)
for child in range(N): 
    if parent[child] != -1:
        graph[parent[child]].append(child)  # 부모 → 자식만 저장


target = int(input())

leaf_count = 0

root = parent.index(-1)


def dfs(node) :
    global leaf_count
    if node == target:  # ❌ 삭제된 노드는 탐색하지 않음
        return
    
    #자식 노드가 없는 경우 = 리프 노드
    if not graph[node]:
        leaf_count += 1
        return
    
    is_leaf = True
    for child in graph[node]:
        if child != target:
            dfs(child)
            is_leaf = False
            
    if is_leaf:
        leaf_count += 1
        
        
if target != root :
    dfs(root)
    print(leaf_count)
else :
    print(0)
