# N-Queen (9663번)

## 🗂️ 문제 링크

[https://www.acmicpc.net/problem/9663](https://www.acmicpc.net/problem/9663)

## 🧩 문제 요약

- N x N 체스판에 N개의 퀸을 서로 공격하지 않도록 배치하는 경우의 수 구하기

## 🔑 핵심 조건

- 행(row), 열(col), ↘ 대각선(i-j), ↗ 대각선(i+j) 중 하나라도 충돌 시 배치 불가
- DFS + 백트래킹으로 모든 유효한 배치 탐색
- 기저조건: row == N일 때 경우 수 +1

## 🚀 구현 포인트

- visited_col 배열 (1차원): 열 점유 여부 체크
- diag1: 좌상→우하(↘) → i-j+(N-1) 값으로 체크
- diag2: 우상→좌하(↗) → i+j 값으로 체크
- 재귀 DFS 구조 사용, 상태 복원(백트래킹) 구현

## ⚠️ 주의할 점

- diag1 / diag2 배열 크기: 2N-1로 정확히 설정 필요
- visited_col, diag1, diag2 모두 **O(1)** 체크 가능 → 효율적 구현
