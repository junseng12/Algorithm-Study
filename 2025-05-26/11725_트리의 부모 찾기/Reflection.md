# 💬 Reflection: 트리의 부모 찾기 (BOJ 11725)

## 🧠 1. 접근 과정 요약

- 무방향 간선 정보를 트리로 해석하고, DFS를 이용해 부모 노드를 추적
- 루트 노드를 1로 고정하고, DFS 중 현재 노드를 기준으로 자식 노드의 부모를 기록

## 🔄 2. 시행착오 및 사고 흐름

- 처음에는 입력이 무방향 간선이므로 부모/자식 관계 구분이 명확하지 않았음
- 방문 배열 대신 `parent[node] == 0` 여부로 방문 여부를 판단함
- DFS 재귀가 부모 → 자식으로 흐르며 자연스럽게 추적됨을 체감함

## ✅ 3. 최종 구현 포인트

```python
def dfs(node):
    for next in graph[node]:
        if parent[next] == 0:
            parent[next] = node
            dfs(next)
```
