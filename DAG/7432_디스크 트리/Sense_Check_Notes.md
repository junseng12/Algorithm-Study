# 🧭 감각 노트: 위상 정렬 Topological Sort

## 🎯 핵심 감각

- DAG에서 **순서를 만들어내는 정렬 방식**
- "진입 차수 0" = 지금 당장 처리 가능한 노드
- 진입 차수 감소 → 조건 충족 → 다음 노드 삽입

## 📌 위상 정렬 알고리즘 요약

```python
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for nxt in graph[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)
```
