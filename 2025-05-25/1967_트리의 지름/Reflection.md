# 💬 Reflection: 트리의 지름 (BOJ 1967)

## 🧠 1. 접근 과정 요약

- 처음에는 트리 DP처럼 상태를 정의하여 문제를 풀려고 했지만,
  이 문제는 단순히 “가장 긴 거리”를 구하는 것이 핵심임을 파악
- 트리의 지름을 구하기 위한 **DFS 2회 탐색 전략**을 학습함

## 🔄 2. 시행착오 및 사고 흐름

- 초기에 `dp[node][0]`, `dp[node][1]` 형태로 접근하려 했지만,  
  이는 이진트리 또는 조건 분기형 문제에 적합한 방식이라는 것을 깨달음
- DFS의 본질을 잘 이해하지 못하고 있었음 → 거리 누적 탐색으로써의 DFS 개념을 재정립
- `DFS(node, distance)` 구조에서 **전역변수 갱신 방식**을 통해 가장 먼 노드를 찾는 로직 학습
  - 본인은 누적된 거리를 기록하는 리스트를 선언하여, "최대 값을 가진 인덱스 == 최장 거리의 노드" 임을 이용하여 수행

## ✅ 3. 최종 구현 포인트

- DFS 1회 → 임의 노드(1번)에서 가장 먼 노드 A 탐색
- DFS 2회 → A에서 가장 먼 노드 B 탐색 → 지름 도출
- 거리 누적은 `distance + weight`로 처리, `max_distance` 변수로 최대값 추적

## 🎯 4. 한 줄 회고

> “DFS의 구조적 역할을 이해하고, 조건 분기 없는 거리 탐색의 감각을 익혔다.”
