# 🧭 감각 노트: DFS + wrap-around + Map 전처리

## 🎯 목적

- DFS로 문자열을 생성하고, Map으로 생성 횟수 누적
- 이후 query에 O(1)로 빠르게 응답

## 📌 구조 요약

```python
dfs(x, y, depth, s):
count_map[s] += 1
if depth == MAX_LEN: return
for 8 directions:
nx = (x+dx+N)%N, ny = ...
dfs(nx, ny, depth+1, s + board[nx][ny])
```

## 🔍 핵심 포인트

- **depth 제한** (`MAX_LEN` = 최대 query 길이)
- **wrap-around**: 모듈로 계산
- **visited 미사용**: 재방문 허용
- **Map 누적 후 O(1) query**

## ⚠️ 주의

- 문자열 start `depth=1, s=board[x][y]`에서 시작해야 누락 없음
- `board`는 char matrix로 입력
- `count_map.get(query,0)`로 없을 때 0 반환
