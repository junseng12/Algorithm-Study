# Problem: 14725_개미굴
# Date: 2025-07-21
# Language: Python 3

# 조건
# 개미굴의 각 층에 먹이가 있는 방을 따라 내려가다 더 이상 내려갈 수 없으면 그 자리에서 움직이지 않고 신호를 보냄
# 로봇 개미는 개미굴 각 층을 따라 내려오면서 알게 된 각 방에 저장된 먹이 정보를 윤수한테 알려줌
# 다음은 로봇 개미들이 윤수에게 보내준 정보
# KIWI BANANA
# KIWI APPLE
# APPLE APPLE
# APPLE BANANA KIWI

# >> 다음과 같이 표현
# APPLE
# --APPLE
# --BANANA
# ----KIWI
# KIWI
# --APPLE
# --BANANA
# 개미굴의 각 층은 "--" 로 구분을 하였다. 또 같은 층에 여러 개의 방이 있을 때에는 사전 순서가 앞서는 먹이 정보가 먼저 나온

# 가정
## 입력 ##
# 첫 번째 줄: 로봇 개미가 각 층을 따라 내려오면서 알게 된 먹이의 정보 개수 N (1 ≤ N ≤ 1000)
# 두 번째 줄~ (N+1)번째 줄: 각 줄의 시작은 로봇 개미 한마리가 보내준 먹이 정보 개수 K (1 ≤ K ≤ 15) , K개의 먹이 정보(왼쪽부터 순서대로 각 층마다 있는 먹이 정보) (먹이 이름 길이 t: 1 ≤ t ≤ 15)

## 출력 ## 
# 개미굴의 시각화된 구조 출력

# 아이디어 
# ## Q1. 🧩 삽입(insert) 구조 — Trie에 데이터를 어떻게 넣어야 할까?

# * **생각해보기**:

#   * 각 개미의 경로는 리스트 형태야 (`["APPLE", "BANANA", "KIWI"]` 등).
#   * root 노드부터 시작해, 리스트의 각 요소를 순회하며 `children` 맵에 없으면 forking해서 새 Node 생성 → 그 노드로 이동.
# * **예시**:

#   ```python
#   curr = root
#   for food in path_list:
#       if food not in curr.children:
#           curr.children[food] = Node(food)
#       curr = curr.children[food]
#   ```

# ---



import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.is_terminal = False


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    # 문자열 삽입
    def insert(self, string):
        curr_node = self.head

        # 삽입할 String 각각의 문자에 대해 자식Node를 만들며 내려간다.
        for char in string:
            # 자식Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            # 같음 문자가 있으면 노드를 따로 생성하지 않고, 해당 노드로 이동
            curr_node = curr_node.children[char]
        curr_node.is_terminal = True

    # 문자열이 존재하는지 탐색!
    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        # 탐색이 끝난 후에 해당 노드의 data값이 존재한다면
        # 문자가 포함되어있다는 뜻이다!
        if curr_node.data is not None:
            return True
        
def dfs(node, depth):
        # 영어 문자열 순으로 우선 순위 (node.children 정렬 처리)
        for char in sorted(node.children):
            print("--" * depth + char)
            child = node.children[char]
            dfs(child, depth+1)
        return

N = int(input())

# 각 정보 입력받아 Trie 구조에 바로 넣기
trie = Trie() 
# 각 입력받은 정보는 연결된 한 경로 내 정보이다. => 아예 데이터 넣을 떄 리스트로 받고, 이후 이어붙여가면서 진행
for _ in range(N):
    data = input().split()       # ['4','A','B','C','D']
    K = int(data[0])             # 4
    foods = data[1:]               # ['A','B','C','D']
    trie.insert(foods)

dfs(trie.head, 0)