# Problem: 2252_줄 세우기
# Date: 2025-07-24
# Language: Python 3

# 조건
# N 명의 학생들을 키 순서대로 줄 세우기
# 마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용
# 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해봄

# 가정

## 입력 ##
# 첫째 줄: 학생 수 N(1 ≤ N ≤ 32,000), 키를 비교한 횟수: M(1 ≤ M ≤ 100,000)
# ~다음 M개의 줄: 키를 비교한 두 학생의 번호 A, B (이는 학생 A가 학생 B의 앞에 서야 한다는 의미)


## 출력 ## 
# 첫째 줄에 학생들을 앞에서부터 줄을 세운 결과
# 답이 여러 가지인 경우에는 아무거나 출력

# 아이디어 
# A -> B 정보만 제시해줌. 적어도 A가 B보다는 먼저와야 한다는 것
# 부분 우숸순위 - 근데 전체 우선순위를 알 수 없으니.. 주어진 것만으로 확인해야 함 
# => 위상 정렬을 공부하고 푸니까 DAG구조에 Queue를 사용한다는 방법을 통해 풀려고 하게 되는데,
# 사실 DAG를 굳이 사용해야 하는 이유는 잘 모르겠음
# 전체 순서에 대한 내용을 구해야 함 -> 정렬 알고리즘 (위상 정렬)

# ⚙️ Q1. 어떤 구조를 써야 하지?
# 어떤 자료구조를 써야 그래프 + 진입 차수 관리를 동시에 할 수 있을까?
# 일단 DAG라는 데이터 구조를 이루는데, 내가 Queue 에 대한 접근이 dfs 에 대한 DAG 구현보다 이해하기 편하여
# 그리고 DFS 처리하는 건 전수 조사나 조건에 맞는 것 찾기 등이니까 이 문제에 어울리지 않는 것 같아서
# Queue 사용하고자 함

# ⚙️ Q2. 진입 차수는 왜 필요한가?
# 즉, "지금 당장 배치 가능한 노드"를 의미함.
# 진입 차수는 이것을 선택하기 위해 선행되는 어떤 것도 없다. 라는 의미를 나타내는 값이다
# 따라서 DAG에서 Queue 자료 구조를 통해 우선순위를 배치할 때 꼭 필요한 정보이다


# ⚙️ Q3. 큐에는 어떤 노드를 먼저 넣어야 할까?
# 진입 차수가 0인 노드를 먼저 넣어야 함

# ⚙️ Q4. 정답 배열은 어떻게 구성될까?
# Queue에서 먼저 넣은 노드를 하나씩 빼면서, 정답리스트에 기록합니다.
# 노드를 빼면서 연관된 노드의 진출 차수를 줄이고 이 변화로 인해 진입 차수가 0이 된 노드를 넣는 과정을 거침


import sys
from collections import deque
input = sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.is_terminal = False


# v: 노드(정점) 개수(N), e: 간선(규칙) 개수(M)
N, M = map(int, input().split())

indegree = [0] * (N + 1)

# graph[u]: u -> ... 로 이어지는 다음 노드 리스트(인접 리스트)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)   # a -> b 간선 저장
    indegree[B] += 1     # b로 들어오는 간선 1 증가

def topology_sort():
    result = []        # 최종 순서 담을 리스트
    q = deque()

    # 3-1. 시작점 찾기: 진입차수 0인 노드들을 큐에 담는다
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    # 3-2. 큐가 빌 때까지 반복
    while q:
        now = q.popleft()     # 0차수 노드 하나 꺼내서
        result.append(now)    # 결과 순서에 넣고

        # 3-3. now와 연결된 간선 제거 효과 주기
        for nxt in graph[now]:
            indegree[nxt] -= 1    # nxt의 진입차수 1 감소
            if indegree[nxt] == 0:
                q.append(nxt)     # 새롭게 0이 된 노드 큐에 삽입
    # 만약 result 길이가 v가 아니라면(사이클 존재), DAG가 아님
    print(*result)

topology_sort()
