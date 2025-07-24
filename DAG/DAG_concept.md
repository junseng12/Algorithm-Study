# 🧠 Concept: Directed Acyclic Graph (DAG) 및 Topological Sorting

---

## 🌳 1. DAG (Directed Acyclic Graph)

- **정의**  
  사이클이 없는 방향 그래프. 즉, 방향을 따라 정점들을 따라 연결했을 때 결코 원형으로 돌아오지 않는 구조
- **특징**
  - 모든 DAG는 **적어도 하나의 위상 정렬**을 가진다
  - 위상 정렬이 존재한다면, 그래프는 반드시 DAG이다.
  - DAG는 부분 순서(partial order)를 나타내며, 위상 정렬은 이를 확장한 선형 순서(linear extension)이다

---

## 🔀 2. Topological Sort (위상 정렬)

※ DAG (Direct Acyclic Graph) : 순환하지 않는(=사이클이 없는) 방향 그래프

- **정의**  
  간선 (u → v)이 존재할 경우, u가 v보다 항상 앞에 오도록 정점들을 선형 순서로 나열하는 것

- **조건**

  - 그래프에 **사이클이 없어야** 하며, 방향성이 중단되지 않도록 정렬해야 한다

- **특징**
  위상 정렬에서는 여러 가지 답이 존재할 수 있다. 한 단계에서 큐에 새롭게 들어가는 원소가 2개 이상인 경우가 있다면, 여러 가지 답이 존재할 수 있다

  ※결과가 유일한 경우

  - 위상 정렬이 유일하려면, 모든 인접 정점 쌍이 Hamilton 경로를 형성해야 한다

모든 원소를 방문하기 전에 큐가 비게 된다면 사이클이 존재한다고 판단할 수 있다. 왜냐하면 사이클에 포함된 원소 중에서 해당되는 어떠한 원소도 큐에 들어가지 못하게 되기 때문이다.

- **정리**: 모든 DAG는 진입차수가 0인 정점(source)를 반드시 가진다
- **귀납법 증명**: 그 정점을 제외한 하위 그래프에 위상 정렬을 적용하고 앞에 삽입함 → 전체 정렬 완성

## 보통 큐로 구현하나, 스택을 이용한 DFS를 이용해 위상 정렬을 구현할 수도 있다.

## ⚙️ 3. 위상 정렬 알고리즘

1. 각 노드의 **진입차수(in-degree)**를 계산
2. 진입차수가 0인 노드들을 **큐에 삽입**
3. 큐에서 꺼낸 노드는 결과 배열에 순서대로 추가
4. 해당 노드의 모든 **자손 노드의 진입차수를 감소**
5. 새롭게 0이 된 노드는 다시 큐에 삽입
6. 큐가 빌 때까지 반복 → 모든 노드가 처리되면 위상 정렬 완료

### Queue를 이용한 방식(카한 방식)

```python
import sys
from collections import deque
input = sys.stdin.readline

# 0. 입력 ----------------------------------------------
# v: 노드(정점) 개수, e: 간선(규칙) 개수
v, e = map(int, input().split())

# 1. 자료구조 준비 --------------------------------------
# indegree[i]: i번 노드로 '들어오는' 간선의 수(진입차수)
indegree = [0] * (v + 1)
# graph[u]: u -> ... 로 이어지는 다음 노드 리스트(인접 리스트)
graph = [[] for _ in range(v + 1)]

# 2. 간선 입력 & 진입차수 계산 ---------------------------
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)   # a -> b 간선 저장
    indegree[b] += 1     # b로 들어오는 간선 1 증가

# 3. 위상 정렬 함수 --------------------------------------
def topology_sort():
    result = []        # 최종 순서 담을 리스트
    q = deque()

    # 3-1. 시작점 찾기: 진입차수 0인 노드들을 큐에 담는다
    for i in range(1, v + 1):
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

    # 4. 출력 --------------------------------------------
    # 만약 result 길이가 v가 아니라면(사이클 존재), DAG가 아님
    print(*result)

topology_sort()

```

### 스택을 이용한 DFS 방식

```python
import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 늘리기 (그래프가 클 때 대비)

# 0. 입력 ----------------------------------------------
input = sys.stdin.readline
N, M = map(int, input().split())

# 1. 자료구조 준비 --------------------------------------
# adj[u]: u -> ... 로 이어지는 다음 노드들
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    adj[A].append(B)

# visited[i]: 방문 여부 표시
visited = [False] * (N + 1)
# order: DFS 종료 시점(모든 후행 노드 처리 완료 시점)에 노드를 넣을 리스트
order = []

# 2. DFS 정의 -------------------------------------------
def dfs(u):
    visited[u] = True           # u 방문 체크
    for v in adj[u]:            # u에서 갈 수 있는 정점들 확인
        if not visited[v]:      # 아직 방문 안 했다면
            dfs(v)              # 깊이 들어감(재귀)

    order.append(u)             # 더 갈 곳 없을 때 '끝난 순서'로 push

# 3. 모든 노드에 대해 DFS 시도 ---------------------------
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)

# 4. 뒤집어서 출력 --------------------------------------
# order에는 "종료한 순서"가 쌓였으므로 역순이 위상 정렬 결과
print(*reversed(order))

```

### ✅ 시간 및 공간 복잡도

- 시간 복잡도: O(|V| + |E|)
- 공간 복잡도: 진입차수 배열 + 큐 + 그래프 인접 리스트

---

## ⚠️ 4. 싸이클 검출 및 적용 조건

- 큐가 텅 비었는데 모든 노드를 처리하지 못하면 → **사이클 존재**
- DAG 아니면 → 위상 정렬 불가능.

---

## 💼 5. 주요 응용 사례

- **컴파일러**: 의존성 모듈 빌드 순서
- **강의 순서**: 선수 과목 기반 수강 흐름
- **작업 스케줄링**: 선후 작업 간 순서 결정
- **위상 정렬 기반 ZKP 회로 구성**: 회로 종속성 정리
- **스프레드시트 재계산 순서**, **Makefile** 순서 결정

---

## 🧩 6. 위상 정렬의 변형

- **DFS 방식**: DFS 완료 순서의 역순이 위상 정렬 (Stack 방식 활용)
- **모든 위상 정렬 출력**: 백트래킹과 branch-and-bound 이용 (ex. BFS + 깊이 우선 탐색)

---

## 📝 요약

- DAG = 방향 + 비순환
- 위상 정렬 = DAG 노드의 "의존성 우선 선형 순서"
- 기본 알고리즘: Queue 방식 (Kahn's algorithm), DFS 방식도 가능
- 다양한 시스템/보안/스케줄링 분야에서 응용 가능

---

## 📚 참고 및 추가 학습 자료

- Wikipedia – Topological sorting, DAG
- GeeksforGeeks – 위상 정렬 예제 및 DFS/BFS 비교
- Tistory/Velog 블로그 – 알고리즘 흐름 및 개념 시각화 : https://velog.io/@kimdukbae/%EC%9C%84%EC%83%81-%EC%A0%95%EB%A0%AC-Topological-Sorting
