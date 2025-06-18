# 💬 Reflection: 노드 사이의 거리 (BOJ 1240)

## 🧠 1. 접근 과정 요약

- 트리에서 두 정점 간 거리 = 경로 상 간선 가중치 누적
- DFS로 두 정점 사이 경로를 탐색하며 거리 누적
- BFS, Dijkstra도 고려했지만 트리 구조에서는 DFS가 가장 직관적

## 🔄 2. 시행착오 및 사고 흐름

- 처음에는 Dijkstra도 고려했으나, 모든 edge weight가 1 이상이고 트리라는 점에서 DFS가 더 적합
- `visited`, `dist` 배열을 매 쿼리마다 초기화하는 구조로 구현
- 메모이제이션 방식도 고려하여 dist 배열 이용하여 풀었음
- 다만, 쿼리 수가 많지 않아 경로 찾자마자 return 하는 형태 추천함(DFS 반복 방식 유지)

```python
def dfs(current, target, visited, distance):
    visited[current] = True
    if current == target:
        return distance

    for adj, weight in graph[current]:
        if not visited[adj]:
            result = dfs(adj, target, visited, distance + weight)
            if result is not None:
                return result
    return None

for _ in range(M):
    u, v = map(int, input().split())
    visited = [False] * (N+1)
    print(dfs(u, v, visited, 0))


```

## ✅ 3. 최종 구현 포인트

```python
def dfs(current, target, distance):
    visited[current] = True
    dist[current] = distance
    if current == target:
        return
    for adj, weight in graph[current]:
        if not visited[adj]:
            dfs(adj, target, distance + weight)
```

## 🚩 4. 시간/공간 복잡도

- 시간 복잡도: O(N) per query

- 공간 복잡도: O(N) (visited[], dist[])
