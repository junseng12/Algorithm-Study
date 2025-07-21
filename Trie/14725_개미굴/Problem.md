# ➕ Problem: 개미굴 (BOJ 14725)

🔗 https://www.acmicpc.net/problem/14725

## 📌 문제 요약

- N개의 먹이 경로(문자열 리스트)가 주어짐
- Trie 구조로 각 경로를 저장
- root부터 DFS로 사전순으로 정렬된 형태로 출력
- depth마다 `--`를 반복해 들여쓰기 출력

## 🔢 입력

- 첫 줄: N (1 ≤ N ≤ 1000)
- 다음 N줄: K (경로 길이) + K개의 문자열

## 🎯 출력

- root부터 각 branch를 사전순으로 출력 (들여쓰기)

## 🧠 핵심 전략

1. Trie 자료구조 설계
2. insert: Node, children dict 사용
3. DFS 출력: sorted()로 사전순, depth별 출력
