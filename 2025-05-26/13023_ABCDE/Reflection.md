# 💬 Reflection: ABCDE (BOJ 13023)

## 🧠 1. 접근 과정 요약

- DFS를 이용해 깊이 5의 단순 경로가 존재하는지를 확인하는 구조라고 판단
- 무방향 그래프이므로 양방향 간선으로 처리하고, 모든 노드를 시작점으로 DFS 수행
- DFS 깊이 도달 조건을 `depth == 5`로 제어

## 🔄 2. 시행착오 및 사고 흐름

- DFS를 진행할 때 `visited[node] = True` 설정 후,  
  재귀 호출 뒤에 `visited[node] = False`로 복원하지 않으면  
  다른 경로에서의 탐색이 막힌다는 점을 캐치
- DFS 깊이 제한이 있다는 점을 잊고 무한 재귀에 빠질 수 있었음
- `exit(0)`을 활용해 빠른 종료 조건 처리하는 실전 팁 적용

## ✅ 3. 최종 구현 포인트

```python
def dfs(node, depth):
    if depth == 5:
        print(1)
        exit(0)
    visited[node] = True
    for next in graph[node]:
        if not visited[next]:
            dfs(next, depth + 1)
    visited[node] = False
```
