# 📌 Sense Check Notes - BOJ 1197

## 1️⃣ 왜 visited 배열이 필요 없는가?

- Kruskal 알고리즘은 "간선 중심"으로 MST를 구성
- 사이클 여부는 Disjoint Set으로 판별 → 노드 방문 여부를 따로 관리할 필요 없음

## 2️⃣ Disjoint Set에서 parent 리스트는 왜 자기 자신으로 초기화?

- 처음에는 모든 노드가 독립적인 집합 → parent[x] = x
- Union 연산으로 집합을 점차 합쳐 나가며 MST 구성
- Find 연산에서 경로 압축 최적화 필수 적용 → 성능 향상

## 3️⃣ MST 종료 조건은 무엇인가?

- MST는 반드시 V-1개의 간선으로 구성됨
- 따라서 edge_count == V - 1 되면 MST가 완성되고 탐색 종료

## 4️⃣ Kruskal에서 정렬 후 pop()을 쓰면 안 되는 이유?

- sort() 후 pop()을 쓰면 "가중치 큰 간선부터 처리"됨 → MST 구성 실패
- **for 루프 순차 처리**가 안전하고 성능도 더 우수

## 5️⃣ 핵심 교훈

- Kruskal 구현 흐름:
  - 간선 입력 → edges 정렬
  - parent 리스트 초기화
  - edges 순차 처리 → 사이클 방지 확인 후 Union → MST 구성
- Disjoint Set 개념 완전히 이해
- visited 처리 없는 MST 설계 감각 체득
