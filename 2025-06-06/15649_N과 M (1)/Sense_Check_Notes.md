# 🧠 Sense_Check_Notes.md: DFS + 백트래킹 사고 흐름

## ✅ 1. 상태 변수는 언제 전역 / 매개변수?

| 조건                                       | 전역 변수 사용 | 매개변수 사용 |
| ------------------------------------------ | -------------- | ------------- |
| 상태 변화가 작고, append/pop으로 복구 가능 | 가능           | 가능          |
| DFS 단계마다 다른 값 필요                  | ❌ 위험        | ✅ 안전       |

---

## ✅ 2. DFS 매개변수 판단 기준

- DFS 단계마다 변화하는 값 → ✅ 매개변수로 설정
- 공통 상태이자 복구가 필요한 값 → 전역 + 복구 방식 사용 가능
- 예: depth, idx, selected, visited, 현재합 등

---

## ✅ 3. DFS 구현 순서

1. **기저 조건** 먼저 검사 → `if depth == M:`
2. **상태 변화** 적용 → visited[i] = True, path.append(i)
3. **DFS 호출** → dfs(depth + 1)
4. **상태 복구** → path.pop(), visited[i] = False

---

## ✅ 4. "모든 경우 탐색"은 반복문 + DFS + 백트래킹

- 부분집합: 각 원소마다 선택 / 비선택
- 순열: visited 체크 → append → dfs → pop
- 경로 탐색: visited로 순회 여부 판단, 조건 분기로 경로 결정

---

## ✅ 5. DFS 실수 줄이기 위한 팁

- 상태 변수는 list면 pop(), bool이면 False로 복구
- depth 또는 idx는 매개변수로 고정
- “탐색할 수 있는 자식 노드”만 순회

---

## 📌 핵심 코드 패턴

```python
def dfs(depth):
    if depth == M:
        print(' '.join(map(str, path)))
        return
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            path.append(i)
            dfs(depth + 1)
            path.pop()
            visited[i] = False
```

---

## 📘 감각 요약

| 항목             | 적용 방식               |
| ---------------- | ----------------------- |
| 상태 변수 관리   | 전역 가능 (복원 필요)   |
| DFS 매개변수     | depth, idx 등 변화 요소 |
| 기저 조건 위치   | DFS 진입 직후 검사      |
| 상태 복구 타이밍 | DFS 호출 직후 복원      |
