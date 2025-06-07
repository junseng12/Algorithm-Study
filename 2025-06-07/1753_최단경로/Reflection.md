# 💬 Reflection: 최단경로 (BOJ 1753)

## 🧠 1. 접근 과정 요약

- 처음에는 BFS로 풀까 고민 → 가중치가 존재하므로 Dijkstra 필요
- 처음으로 heapq를 활용한 우선순위 큐 사용법을 적용
- distance 배열을 이용해 최단 거리 업데이트 방식 이해

## 🔄 2. 시행착오 및 사고 흐름

- visited 배열을 사용할까 고민했으나, distance 값 비교 방식으로 처리
- 출력 부분에서 INF 처리 로직 처음에 실수 → else 추가하여 해결
- heapq 사용 원리를 사고 흐름 단계에서 정확히 이해함

## ✅ 3. 최종 구현 포인트

```python
heapq.heappush(queue, (0, K))

while queue:
    current_distance, current_node = heapq.heappop(queue)

    if current_distance > distance[current_node]:
        continue

    for adj_node, weight in graph[current_node]:
        if distance[adj_node] > current_distance + weight:
            distance[adj_node] = current_distance + weight
            heapq.heappush(queue, (distance[adj_node], adj_node))
```

## 🚩 4. 시간/공간 복잡도

- 시간 복잡도: O(E log V)
- 공간 복잡도: O(V + E)

### visited 배열 왜 불필요한가?

- distance\[current_node]보다 더 긴 거리로 pop된 경우 continue 처리
- 이 방식으로 visited 역할을 자연스럽게 대체 가능

## ✅ 5. 핵심 교훈

- Dijkstra 구현의 핵심은 "우선순위 큐 관리 + distance 업데이트 패턴" 이해
- 처음에는 BFS와 혼동하기 쉽지만, 가중치가 존재하는 순간 Dijkstra 사고 패턴으로 전환해야 함
