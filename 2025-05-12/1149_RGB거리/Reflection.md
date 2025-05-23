# 💬 Reflection: RGB 거리 (BOJ 1149)

## 🧠 1. 접근 과정 요약

- i번째 집을 R/G/B 중 하나로 칠할 때,  
  이전 집은 그 색이 아니어야 한다는 조건에서 **상태 분리**가 필요함을 인식
- `dp[i][c] = i번째 집까지 색칠했을 때, i번째 집을 색상 c로 칠한 최소 비용`으로 상태 정의
- 점화식:
  - `dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + cost[i][R]` 등으로 전개

## 🔄 2. 시행착오 및 사고 흐름

- 처음에는 단일 차원 dp로 표현하려다 상태가 섞이는 문제 발생
- 색상을 기준으로 상태를 나누는 방식으로 구조를 재설계
- 수치 예제를 직접 대입하면서 점화식을 검증하고 신뢰도 확보

## ✅ 3. 최종 구현 포인트

- 초기값 설정: `dp[0] = cost[0][:]`
- 색상 간 중복을 피하기 위한 분기: min(다른 두 색)
- 정답은 `min(dp[N-1])`

## 💡 4. 보완 아이디어

- 메모리를 줄이려면 `dp` 없이 `cost` 배열 자체를 갱신하는 방법도 가능
- 실전에서는 3개의 변수를 이용한 슬라이딩 윈도우 방식도 효율적

## 🔁 5. 복습 포인트

- 조건 기반 DP는 **상태를 나누는 기준을 명확히 세우는 것**이 핵심
- 이차원 DP를 사용할 때는 각 축의 의미를 명확히 구분하자

## ✍️ 6. 한 줄 소감

> “선택지는 항상 있다 — 조건을 나누면 최선의 선택이 보인다.”
