# ➕ Problem: 문자열 지옥에 빠진 호석 (BOJ 20166)

🔗 https://www.acmicpc.net/problem/20166

## 📌 문제 요약

- N×M 격자에서 알파벳을 이동하며 최대 길이 5의 문자열 조합 생성
- wrap-around 이동 (경계 넘어가면 반대편으로 연결)
- K개의 query 문자열에 대해 해당 문자열이 만든 경로 수 출력

## 🔢 입력

- 첫 줄: N M K (3 ≤ N, M ≤ 10, 1 ≤ K ≤ 1000)
- 다음 N줄: M개의 소문자 알파벳
- 마지막 K줄: query 문자열 (1~5 글자, 중복 가능)

## 🎯 출력

- 각 query 문자열마다 생성된 경로 수 출력

## 🧠 핵심 전략

1. **DFS**로 모든 시작점에서 문자열 탐색 (길이 ≤ max_query_len)
2. 가능한 모든 문자열을 `count_map[string] += 1`로 저장
3. 각 query에 대해 `count_map.get(query, 0)`으로 결과 출력
