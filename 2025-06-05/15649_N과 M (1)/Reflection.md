# 💬 Reflection: N과 M (1) (BOJ 15649)

## 🧠 1. 접근 과정 요약

- 순열 구성 문제로, DFS를 이용해 한 자리씩 수를 채워나가기로 결정
- 백트래킹으로 이미 사용한 수는 제외하고, 수열에서 빠질 경우 복구 필요

## 🔄 2. 시행착오 & 사고 흐름 정리

- 처음에는 DFS 함수에 `path`를 전역으로 뒀다가 예기치 않은 동작 발생
- DFS 함수 내에서 수를 추가한 후 탐색하고, 이후 `pop()`으로 복원해야 함
- visited 복원 타이밍을 잘못 두면 중복된 수가 포함됨

### ✅ Q1. `selected`, `used` 같은 상태 변수는 언제 전역 vs 매개변수로 둘까?

- 상태가 DFS 단계별로 달라지고, 복구가 필요하면 매개변수로 두는 것이 안전.
- 하지만 리스트에 `append → dfs → pop` 구조로 사용한다면 전역으로 둬도 무방.
- 이 문제에서는 `visited`는 전역, `path`는 append/pop을 사용해 매개변수로 관리 추천.

### ✅ Q2. DFS의 매개변수로 둘 수 있는 것은 무엇인가?

- DFS 재귀마다 달라지는 값(ex. depth, 현재 선택된 수)은 매개변수로 둔다.
- 공통 상태(visited, path)는 전역으로 관리하되 백트래킹 시 복원 필요.
- 예: `dfs(depth)` → depth는 단계마다 달라지므로 매개변수로 사용.

### ✅ Q3. DFS 기저 조건 → 상태 복구 순서

- 기저 조건 먼저 체크 (`depth == M`)
- 상태 변경: path.append(i), visited[i] = True
- DFS 재귀 호출
- 상태 복구: path.pop(), visited[i] = False

---

## ✅ 3. 최종 구현 포인트

```python
def dfs(depth, path):
    if depth == M:
        print(' '.join(map(str, path)))
        return
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            path.append(i)
            dfs(depth + 1, path)
            path.pop()
            visited[i] = False
```

---

## 4. 배운 점 요약

| 항목             | 적용 방식                              |
| ---------------- | -------------------------------------- |
| DFS 매개변수     | depth                                  |
| 상태 변수 관리   | path(전역), visited(전역, 복원 필요)   |
| 기저 조건        | depth == M                             |
| 상태 복원 타이밍 | DFS 호출 직후 path.pop(), visited 복원 |
