# ➕ Problem: 계단 오르기 (BOJ 2579)

- 링크: https://www.acmicpc.net/problem/2579

## 📌 문제 요약

- 계단은 한 번에 1칸 또는 2칸씩 오를 수 있다.
- 연속된 세 계단을 밟을 수는 없다.
- 마지막 도착 계단은 반드시 밟아야 한다.
- 각 계단에는 점수가 부여되어 있으며, 밟은 계단의 점수 합의 최댓값을 구하라.

## 🔢 입력 조건

- 첫째 줄: 계단의 개수 N (1 ≤ N ≤ 300)
- 둘째 줄부터 N개의 줄: 각 계단의 점수 (10,000 이하 자연수)

## 🎯 출력 조건

- 계단을 오르며 얻을 수 있는 최대 점수를 출력 (단, 마지막 계단은 반드시 밟아야 함)

## 🧠 문제 핵심

- 연속 3계단을 밟을 수 없기 때문에, 조건을 고려한 DP 설계가 필요
- 마지막 계단을 반드시 밟아야 하므로, 최종 출력은 dp[N-1]
- 점화식 설계를 통해 상태 전이 방식 정확히 구성 필요

## 💡 관련 개념

- 조건 제한 Dynamic Programming
- 상태 정의 및 초기값 처리
- 마지막 상태 도달 조건을 포함하는 점화식 구성
