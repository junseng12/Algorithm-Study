# 🧭 감각 노트: Trie + DFS 출력

## 🎯 목적

- 문자열 경로를 Trie로 저장 후
- 모든 branch를 depth별로 출력 (들여쓰기 포함)

## 📌 핵심 구조

```python
def dfs(node, depth):
for key in sorted(node.children):
print("--" \* depth + key)
dfs(node.children[key], depth + 1)
```

## 🔍 체크 포인트

- is_terminal은 종료 조건이 아니다!
- sorted()로 children 사전순 정렬 필요
- depth=0부터 시작, root는 출력 X

## ⚠️ 주의

- dict.sort() 안됨 → sorted()
- leaf 도달 후 자동 backtracking
- 종료조건 = 탐색 종료 X, 함수 끝나며 상위로 복귀

## 💡 기억 키워드

- Trie insert
- DFS 정렬 출력
- depth 기반 출력 포맷
