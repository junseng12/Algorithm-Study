# 🧭 감각 노트: 디렉토리 Trie + DFS 출력

## 🎯 목적

- Trie는 문자열 검색뿐만 아니라 **경로 기반 계층 구조** 표현에 매우 유용함.
- DFS를 활용한 계층적 출력 → 각 노드의 정렬과 depth 제어가 핵심.

## 📌 구조 요약

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.children = {}

def insert(root, path):
    for part in path:
        if part not in root.children:
            root.children[part] = Node(part)
        root = root.children[part]

def dfs(node, depth):
    for key in sorted(node.children):
        print(' ' * depth + key)
        dfs(node.children[key], depth + 1)
```
