## ✅ 자료구조 선택 가이드: 상황별, 특성별 정리표

아래는 알고리즘 문제 풀이 시 자주 쓰이는 자료구조들을 **목적**, **특성**, **활용 사례** 중심으로 정리한 것입니다.

---

### 📚 기본 리스트/배열 (`list`)

| 항목          | 설명                                                                  |
| ------------- | --------------------------------------------------------------------- |
| **사용 목적** | 순차 데이터 저장, 인덱싱                                              |
| **특성**      | 인덱스 접근 `O(1)`, 삽입/삭제 `O(n)`                                  |
| **유용할 때** | 정렬된 순서를 유지해야 할 때, DP 테이블, 거리 기록, 단순 스택/큐 역할 |
| **예시 문제** | DP (`dp[]`), 거리배열 (`dist[]`), 카운팅 배열, 부분합                 |

---

### 🗃️ 딕셔너리 (`dict` / `defaultdict`)

| 항목          | 설명                                                                                      |
| ------------- | ----------------------------------------------------------------------------------------- |
| **사용 목적** | 키-값 매핑                                                                                |
| **특성**      | 키 기반 접근 `O(1)`, 유연성, 빠른 검색                                                    |
| **유용할 때** | 그래프 인접 리스트, 해시맵 카운팅, 메모이제이션                                           |
| **예시 문제** | 그래프 저장 (`graph[u] = [(v, w)]`), 카운트 (`dict[char] += 1`), Trie 구현 시 `dict` 활용 |

---

### 📦 집합 (`set`)

| 항목          | 설명                                                              |
| ------------- | ----------------------------------------------------------------- |
| **사용 목적** | 중복 제거, 빠른 포함 여부 판단                                    |
| **특성**      | 삽입/삭제/탐색 모두 평균 `O(1)`                                   |
| **유용할 때** | 방문 여부 추적, 유니크한 원소 추출                                |
| **예시 문제** | 사이클 검출, 유니온 파인드 중 루트 저장, 문자열 조합 중 중복 제거 |

---

### 🧰 큐 (`collections.deque`)

| 항목          | 설명                                      |
| ------------- | ----------------------------------------- |
| **사용 목적** | 선입선출 구조 (FIFO)                      |
| **특성**      | `deque`은 양방향 `O(1)` 삽입/삭제 지원    |
| **유용할 때** | BFS, 다익스트라, 슬라이딩 윈도우          |
| **예시 문제** | BFS, 토마토 문제, 레벨 탐색, BFS 거리계산 |

---

### 🎛️ 우선순위 큐 (`heapq`)

| 항목          | 설명                                           |
| ------------- | ---------------------------------------------- |
| **사용 목적** | 최소/최대 우선순위 추출                        |
| **특성**      | 삽입/삭제/탐색 `O(log n)`                      |
| **유용할 때** | 다익스트라, K번째 수, 힙 정렬                  |
| **예시 문제** | 다익스트라, 힙 기반 스케줄링, 작업 처리 최적화 |

---

### 🎯 스택 (`list` 또는 `deque`)

| 항목          | 설명                                  |
| ------------- | ------------------------------------- |
| **사용 목적** | 후입선출 구조 (LIFO)                  |
| **특성**      | `append()` + `pop()` 조합             |
| **유용할 때** | DFS, 괄호 매칭, 백트래킹              |
| **예시 문제** | DFS, 괄호 짝 검사, 백트래킹 순회 경로 |

---

### 🌐 그래프 인접 리스트 (`dict` or `list` of lists)

| 항목          | 설명                                   |
| ------------- | -------------------------------------- |
| **사용 목적** | 노드 간 연결 관계 표현                 |
| **특성**      | `graph[u].append((v, w))`              |
| **유용할 때** | 모든 그래프 문제의 기본 구조           |
| **예시 문제** | DFS/BFS, 다익스트라, 위상정렬, 트리 DP |

---

### 📊 트리 구조 (배열 기반 or 클래스 기반)

| 항목          | 설명                                                                 |
| ------------- | -------------------------------------------------------------------- |
| **사용 목적** | 계층적 데이터 구조, 유일 경로 보장                                   |
| **특성**      | 간선 `N-1`, 루트부터 하향식 순회                                     |
| **유용할 때** | DP on Tree, 트리 지름, 서브트리 처리                                 |
| **예시 문제** | 1967 트리의 지름, 최소 공통 조상(LCA), 세그먼트 트리, 이진 탐색 트리 |

---

## 🔁 선택 가이드 요약

| 상황                            | 추천 자료구조                  |
| ------------------------------- | ------------------------------ |
| 단순 순회 / DP 배열             | `list[]`                       |
| 그래프 탐색                     | `dict` (or `list of lists`)    |
| 중복 제거 / 빠른 탐색           | `set`                          |
| BFS                             | `deque`                        |
| DFS                             | `stack` (`list`) or 재귀       |
| 우선순위 기반 처리              | `heapq`                        |
| 문자열 탐색 (빠른 조합, 카운팅) | `dict` + `set`                 |
| 트리 구조 표현                  | `dict[u].append((v, w))` + DFS |

---

## 🎯 실전 전략: 문제 유형별 추천 구조

| 문제 유형                       | 추천 자료구조                                        |
| ------------------------------- | ---------------------------------------------------- |
| **트리의 지름 / DFS 경로 누적** | `graph = defaultdict(list)` + `visited[]` + `dist[]` |
| **최단 경로 (가중치)**          | `graph + heapq` (다익스트라)                         |
| **BFS 기반 거리 측정**          | `deque`, `dist[]`                                    |
| **DP with 상태 저장**           | `dp[][]`, `memo = dict()`                            |
| **그래프 사이클 검출**          | `visited`, `parent`, `set`                           |
| **문자열 조작 및 빈도 수 체크** | `dict` + `Counter`                                   |
| **슬라이딩 윈도우 최댓값**      | `deque`                                              |

---

## 🧠 기억법 TIP

> 📌 "문제의 목적 = 자료구조 선택 기준"

- ✅ 빠르게 찾고 싶은가? → `dict`, `set`, `heap`
- ✅ 순서를 유지하고 싶은가? → `list`, `deque`
- ✅ 구조가 트리인가? → `DFS` + `graph` + `visited` + `parent`

---

훌륭한 전략이에요, Junseung!
자료구조를 제대로 이해하면 **문제 해결의 50%는 이미 끝난 것**이라고 해도 과언이 아니죠.
당신이 앞으로 어떤 문제를 만나더라도 **스스로 상황에 맞는 자료구조를 설계하고 선택할 수 있도록**, 다음과 같이 정리해드릴게요:

---

## 🧠 자료구조 총정리: 상황별 활용 & 특성 비교표

| 자료구조                         | 사용 시기                 | 특성                                  | 시간복잡도                | 활용 예시                    |
| -------------------------------- | ------------------------- | ------------------------------------- | ------------------------- | ---------------------------- |
| **배열 (list)**                  | 순차적 데이터 저장        | 인덱스로 빠른 접근, 고정 크기 가능    | O(1) 접근, O(n) 삽입/삭제 | DP, 슬라이딩 윈도우, 누적합  |
| **리스트 (Python list)**         | 순서 유지, 유연한 길이    | 파이썬에서는 배열보다 범용적으로 사용 | O(1) 접근, O(n) 중간삽입  | 트리 탐색 결과 저장, 큐 역할 |
| **스택 (list or deque)**         | 후입선출 (LIFO)           | 함수 호출 기록, 상태 백트래킹         | O(1) 삽입/삭제            | DFS, 괄호검사, 백트래킹      |
| **큐 (deque or queue.Queue)**    | 선입선출 (FIFO)           | 순서 있는 처리                        | O(1) 삽입/삭제            | BFS, 시뮬레이션, 레벨별 탐색 |
| **덱 (deque)**                   | 양쪽 삽입/삭제            | 큐 + 스택 역할                        | O(1) 양방향               | 슬라이딩 윈도우 최적화       |
| **힙 (heapq)**                   | 우선순위 큐               | 최소/최대값 빠르게 꺼내기             | O(log n) 삽입/삭제        | 다익스트라, K번째 수         |
| **집합 (set)**                   | 중복 제거, 빠른 포함 검사 | 순서 없음, 해시 기반                  | O(1) 평균                 | 방문 처리, 유일성 검사       |
| **딕셔너리 (dict)**              | 키-값 맵핑                | 해시 기반, 빠른 조회                  | O(1) 평균                 | 그래프, 카운팅, 캐싱         |
| **문자열 (str)**                 | 텍스트 처리               | 불변, 슬라이싱 유용                   | O(n)                      | KMP, 라빈-카프, 트라이       |
| **트라이 (Trie)**                | 문자열 집합 저장/탐색     | prefix 빠름, 노드 기반 트리           | O(length)                 | 자동완성, 사전 필터링        |
| **그래프 (dict of list/tuple)**  | 관계 표현                 | 유연한 모델링 가능                    | O(V+E)                    | DFS, BFS, 최단거리           |
| **이진트리 (Node class)**        | 정렬/탐색 트리 구현       | 높이 관리 중요                        | O(log n) (균형 트리 기준) | 세그먼트 트리, 힙, AVL       |
| **세그먼트 트리**                | 구간 쿼리, 구간 갱신      | 재귀적 구조, log 시간                 | O(log n)                  | 구간합, 최대/최소값 쿼리     |
| **유니온 파인드 (Disjoint Set)** | 집합 간 연결 여부 검사    | 경로 압축 사용                        | O(α(n))                   | 사이클 탐지, MST, 그룹화     |

---

## 📌 자료구조 선택 가이드 (상황별 전략)

| 상황                          | 추천 자료구조  | 이유                |
| ----------------------------- | -------------- | ------------------- |
| 순서대로 처리, 중간 삽입 없음 | `list`         | 단순 저장/출력      |
| 순서대로 처리, 중간 삽입 필요 | `deque`        | O(1) 삽입/삭제      |
| 가장 작은/큰 값을 반복 꺼냄   | `heapq`        | 자동 정렬 유지      |
| 중복 제거, 빠른 포함 검사     | `set`          | 해시 기반           |
| 매핑/카운팅이 필요            | `dict`         | 키-값 매핑          |
| 문자열 집합/접두사 탐색       | `Trie`         | O(length) 탐색      |
| 구간의 합/최댓값/최솟값       | `Segment Tree` | O(log n)            |
| 집합 연결/분리, 사이클 검사   | `Disjoint Set` | O(α(n)) (거의 O(1)) |
| 모든 정점 간 최단거리         | `dict + heapq` | Dijkstra 용         |
| BFS, 레벨탐색                 | `deque`        | O(1) 큐             |
| DFS, 백트래킹                 | `stack`, 재귀  | 호출 순서 유지      |

---

## 🧠 연습용 질문 리스트 (감각 점검용)

1. 그래프에서 연결 관계가 주어졌을 때, 양방향 저장은 어떤 구조가 적절할까?
2. 문자열 배열 중 접두사 자동 완성 기능이 필요할 땐?
3. 모든 정점에서 다른 정점까지의 최단 거리 구하려면?
4. 수열의 특정 구간에서 합을 빠르게 구하려면?
5. 서로소 집합 판별과 병합을 빠르게 하려면?

---
