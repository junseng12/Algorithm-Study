# 💬 Reflection: N-Queen (BOJ 9663)

## 🧠 1. 접근 과정 요약

- 처음에는 **visited 2차원 배열 + 대각선 충돌 직접 탐색** 구조로 접근했으나, 수학적으로 ↗ ↘ 대각선이 **i+j, i-j 패턴으로 O(1) 체크 가능**하다는 점을 학습.
- 행(row)은 DFS 깊이 자체로 고정되고, 열(col), ↗, ↘ 방향 대각선만 관리하면 충분하다는 점을 깨달음.
- Queen 개수는 따로 매개변수로 관리할 필요 없이 `row == N` 여부로 완료 여부 판단 가능.

## 🔄 2. 시행착오 및 사고 흐름

- 처음에는 **visited 2차원 배열**, **nochoice 변수**, **queen 개수 따로 관리**하는 설계를 시도.
- 시행착오 중 **col 충돌만 1차원 배열로 처리 가능**하다는 점, **대각선 인덱스의 수학적 정의**를 정확히 이해.
- `diag1` / `diag2` 배열 크기를 `2N-1`로 정확히 잡아야 index error가 발생하지 않는다는 점도 실전 테스트 중 학습.

## ✅ 3. 최종 구현 포인트

- DFS 호출 구조:

  ```python
  def dfs(row):
      if row == N:
          count += 1
          return
      for col in range(N):
          if not visited_col[col] and not diag1[row - col + (N - 1)] and not diag2[row + col]:
              visited_col[col] = diag1[row - col + (N - 1)] = diag2[row + col] = True
              dfs(row + 1)
              visited_col[col] = diag1[row - col + (N - 1)] = diag2[row + col] = False
  ```

- 대각선 인덱스 관리:
  - ↘ 좌상 → 우하: diag1[row - col + (N - 1)]
  - ↗ 우상 → 좌하: diag2[row + col]
