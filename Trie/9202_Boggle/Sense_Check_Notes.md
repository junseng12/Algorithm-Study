# 🧭 감각 노트: DFS + Trie 자동완성 탐색

## 🎯 목적

DFS는 단순 탐색이 아니라,
**"조건을 만족하는 경로만 깊게 들어가는 여정"**으로 이해해야 한다.
Boggle에서는 Trie로 prefix pruning하여 가지치기하며 탐색 효율 극대화.

## 📌 구조 요약

```python
def dfs(x, y, node, word):
    if (범위 밖 or visited): return
    if (board[x][y] not in node.children): return
    next_node = node.children[char]
    if next_node.is_terminal:
        found_words.add(word)
    visited[x][y] = True
    for dir in 8방향:
        dfs(nx, ny, next_node, word + char)
    visited[x][y] = False
```

- prefix pruning → 탐색 공간 줄임
- visited → 같은 자리 중복 방지
- backtracking → 다른 경로 재활용

## 🔍 대표 문제 감각 비교

| 문제            | 핵심 감각                      | DFS 역할                             |
| --------------- | ------------------------------ | ------------------------------------ |
| 9202 Boggle     | Trie + DFS 자동완성, 점수 계산 | prefix pruning, 경로 구성, 중복 방지 |
| 5670 휴대폰자판 | Trie 평균 입력 계산            | branch point 계산, 자동완성          |

## 💡 기억 키워드

- Trie: 조건 압축 탐색의 핵심
- DFS: 경로별 상태 관리, 백트래킹
- set: 중복 탐지/방지

## 🧩 적용 패턴

| 유형           | 패턴                                  |
| -------------- | ------------------------------------- |
| prefix pruning | if char not in node.children → return |
| 결과 누적      | if is_terminal: found_words.add()     |
| 경로 재활용    | visited[x][y] → backtracking          |

## 📂 실전 감각 확장

- Trie + DFS: 빠른 문자열 매칭
- 중복 방지: set, visited
- 후처리: 점수/길이/사전순 비교
