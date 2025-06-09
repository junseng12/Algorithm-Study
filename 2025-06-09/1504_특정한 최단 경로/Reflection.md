# 💬 Reflection: 특정한 최단 경로 (BOJ 1504)

## 🧠 1. 접근 과정 요약

- 처음에는 단일 Dijkstra로 풀 수 있을까 고민
- 반드시 v1, v2를 경유해야 한다는 조건 → Dijkstra 1번으로 불가능
- 여러 번 Dijkstra를 실행하여 경유 조건을 만족시키는 방법으로 전환

## 🔄 2. 시행착오 및 사고 흐름

- heapq 사용 시 (distance, node) 순서를 주의해야 한다는 점 실습 중 발견
- Dijkstra 여러 번 호출 시 distance 배열을 전역이 아닌 local로 관리해야 안정적임을 체감
- INF 체크의 중요성을 다시 확인함 (경로가 없는 경우 처리 필요)

## ✅ 3. 최종 구현 포인트

```python
route1 = d1[v1] + d2[v2] + d3[N]
route2 = d1[v2] + d3[v1] + d2[N]

if route1 == INF or route2 == INF:
    print(-1)
else:
    print(min(route1, route2))
```

## 🚩 4. 시간/공간 복잡도

- 시간 복잡도: O(3 \* E log N)
- 공간 복잡도: O(N + E)
