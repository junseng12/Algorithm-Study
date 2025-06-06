# ➕ Problem: N과 M (1) (BOJ 15649)

- 링크: https://www.acmicpc.net/problem/15649

## 📌 문제 요약

- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 모든 수열을 출력
- 사전 순으로 출력

## 🔢 입력 조건

- 첫째 줄: 자연수 N과 M (1 ≤ M ≤ N ≤ 8)

## 🎯 출력 조건

- 한 줄에 하나씩 문제 조건을 만족하는 수열 출력

## 🧠 문제 핵심

- **순열 (Permutation)**: N개 중 M개를 고르는 모든 경우의 수
- DFS + 백트래킹으로 상태를 구성하며 탐색
- 중복 없이 선택해야 하므로 `visited` 배열이 필요

## 💡 관련 개념

- DFS (재귀)
- 백트래킹
- 순열, 조합
