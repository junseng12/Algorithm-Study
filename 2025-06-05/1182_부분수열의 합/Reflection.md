# 💬 Reflection: 부분수열의 합 (BOJ 1182)

## 🧠 1. 접근 과정 요약

- 처음에는 백트래킹 형태로 접근했지만, 사실은 **포함 여부의 이진 분기(2^N)** 구조라는 것을 깨달음.
- 각 원소의 **선택/비선택**을 기준으로 DFS를 구성했고, 이 과정에서 `idx`와 `current_sum`만으로 상태 정의가 가능함을 확인함.
- 예외적으로 **S == 0**일 때 공집합을 제외하는 처리 필요.

## 🔄 2. 시행착오 및 사고 흐름

- 트리 기반 DFS나 경로 탐색 구조에 익숙해진 상태라, 처음엔 `visited`, `sum` 등 전역 상태 기반 DFS를 설계함.
- 그러나 이 문제는 경로가 아닌 **부분집합 생성 탐색**에 더 가까워 `visited`나 그래프 구조가 필요 없었음.

## ✅ 3. 최종 구현 포인트

- DFS 호출 구조:

  ```python
  def dfs(idx, current_sum):
      if idx == N:
          if current_sum == S:
              count += 1
          return
      dfs(idx + 1, current_sum + numlist[idx])
      dfs(idx + 1, current_sum)
  ```

- 공집합 예외:

  ```python
  if S == 0:
      count -= 1
  ```
