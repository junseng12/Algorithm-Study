# 💬 Reflection: 트리 (BOJ 1068)

## 🧠 1. 접근 과정 요약

- 트리의 구성 정보를 자식 중심으로 재구성하여 DFS를 수행함
- 삭제된 노드를 기준으로 DFS를 우회하도록 처리
- 리프 노드 판별은 **현재 노드의 자식이 모두 삭제되었거나 없는 경우**로 판단

## 🔄 2. 시행착오 및 사고 흐름

- 처음에는 단순히 `tree[node]`가 비어있으면 리프 노드로 판단했지만,
  삭제된 노드가 자식에 있을 경우를 고려하지 않아 오답 발생 가능성 발견
- DFS 중 자식이 삭제 노드인 경우를 분기 조건으로 제외해야 함
- 루트 노드가 삭제된 경우, **탐색 자체를 생략**해야 하는 특수 케이스를 처리함

## ✅ 3. 최종 구현 포인트

```python
def dfs(node):
    if node == deleted:
        return
    if not tree[node] or all(child == deleted for child in tree[node]):
        count += 1
        return
    for child in tree[node]:
        if child != deleted:
            dfs(child)
```
