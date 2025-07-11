# 📌 Sense Check Notes - BOJ 1351

## 1️⃣ 왜 배열 DP 대신 dict인가?

- N 최대 10^12 → 배열 불가능, 해시맵으로 sparse storage.

## 2️⃣ 핵심 로직 점검

- memo[i] = A(i//P) + A(i//Q)
- memo[0]=1로 시작

## 3️⃣ 예외/경계 조건

- i=0에서 무조건 1 반환
- 재귀 깊이 제한 필요 (Python)

## 4️⃣ 더 발전시킬 여지

- iterative DP로 재작성
- C++ unordered_map vs Python dict 성능 비교
