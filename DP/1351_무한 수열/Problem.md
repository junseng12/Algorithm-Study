# ➕ Problem: 무한 수열 (BOJ 1351)

링크: https://www.acmicpc.net/problem/1351

## 📌 문제 요약

A[0]=1, A[i]=A[i//P]+A[i//Q]로 정의된 무한 수열에서 A[N] 값을 구하라.

## 🔢 입력 조건

- N, P, Q (0 ≤ N ≤ 10^12, 1 ≤ P, Q ≤ 10^9)

## 🎯 출력 조건

- A[N] 값 출력

## 🧠 문제 핵심

- N이 매우 커서 배열 DP 불가
- dict로 메모이제이션하며 재귀 호출

## 💡 관련 개념

- DP with memoization
- HashMap (dict)
- 재귀 최적화
