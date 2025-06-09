# 📌 Sense Check Notes - BOJ 1504

## 1️⃣ 왜 Dijkstra 1번만으로는 불가능한가?

- 반드시 v1, v2를 경유해야 하는 조건이 존재 → 단일 Dijkstra로는 경유 여부를 보장할 수 없음
- 따라서 여러 번 Dijkstra를 실행하고 경유 경로를 조합해야 함

## 2️⃣ Dijkstra 몇 번 돌렸는가?

- 1번 정점에서 → dijkstra(1)
- v1 정점에서 → dijkstra(v1)
- v2 정점에서 → dijkstra(v2)
- 총 3번 실행 → 필요한 모든 경유 경로의 거리 계산 가능

## 3️⃣ route1 / route2 구성은 어떻게 했는가?

```python
route1 = d1[v1] + d2[v2] + d3[N]
route2 = d1[v2] + d3[v1] + d2[N]
```

- 둘 중 최소값 출력

## 4️⃣ heapq 사용 시 주의점

- heapq에는 (distance, node) 순서로 넣어야 우선순위가 거리 기준으로 동작함
- 실습 중 직접 발견하고 수정하여 학습

## 5️⃣ INF 체크 포인트

- 경유 경로의 일부라도 INF면 → 전체 경로는 불가능 → -1 출력
- 이 문제에서는 반드시 INF 체크가 필요함

## 6️⃣ 핵심 교훈

- "여러 번 Dijkstra 실행 → 경로 조합 계산" 패턴을 익혔다
- Dijkstra 함수는 항상 distance 배열 local 관리
- heapq 사용 시 push 순서 주의

---
