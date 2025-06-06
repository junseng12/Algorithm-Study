### 📌 감각 메모 (실습 중 질문 기반 정리)

# DFS 백트래킹 감각노트: 알파벳

## 🔁 상태 백트래킹의 핵심

- 상태 백트래킹은 **변수의 값이 변경되었다면 반드시 원상복귀해야 한다**는 원칙을 따른다.
- 여기서는 visited 알파벳을 set으로 관리했기 때문에:
  ```python
  visited.add(board[x][y])
  ...
  visited.remove(board[x][y])
  ```

## 🎯 DFS depth 의미

- DFS 내부에서 `depth`는 **지금까지 밟은 칸 수**를 의미하며,
- 이 값은 경로의 길이를 재는 데 사용되므로, 재귀 호출마다 `depth + 1` 형태로 전달되어야 한다.

## ✅ 탐색 방향(dx, dy)의 패턴

- 상하좌우는 격자 이동의 정석 패턴:

  ```python
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  ```

- 반복문 하나로 이동 좌표를 제어할 수 있어서 가독성도 좋고 오류도 줄일 수 있다.

## 🎯 비트마스크란?

- 길이가 26인 알파벳 배열을 26비트짜리 정수 하나로 표현
- 알파벳 'A'~'Z'는 `ord(char) - ord('A')`로 인덱싱 가능
- 알파벳 `ch`를 사용 중인 상태 → `mask & (1 << ch)`
- 알파벳 `ch`를 추가 → `mask | (1 << ch)`

## ✅ visited[x][y][mask] 메모이제이션

- DFS의 탐색 상태는 좌표 (x, y)와 알파벳 사용 상태 (mask)로 정의됨
- 이전에 (x, y, mask) 상태를 탐색한 적 있다면 그 이후 결과는 동일하므로 다시 탐색할 필요 없음
- 따라서 이 상태를 기록하고 **가지치기 (pruning)** 해야 효율적임

## 🧠 실전 감각 & 실습 중 느낀 점

- 단순한 DFS 문제가 아니라, **조건 상태 관리**가 매우 중요한 문제였다.
- 앞으로 DFS 문제를 풀 때는 단순히 방문 여부 외에도 **문제에 따라 방문 조건을 정확히 정의하고, 상태를 관리하는 자료구조를 설계해야 한다**는 교훈을 얻었다.

- 상태 압축이 필요한 경우: 비트마스크는 거의 최적의 선택
- 백트래킹을 사용할 때, **상태가 유일하게 결정되는 조건**이 있다면 memoization으로 중복 제거 가능
- 다차원 visited 관리에 익숙해져야 대형 문제에서 성능 확보 가능
