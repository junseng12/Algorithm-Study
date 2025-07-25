# ➕ Problem: 줄 세우기 (BOJ 2252)

🔗 https://www.acmicpc.net/problem/2252

## 📌 문제 요약

- 학생들 간의 키 비교 정보가 주어졌을 때, 그에 따라 줄을 세우는 문제.
- 각 관계는 "A는 B보다 앞에 서야 한다"는 단방향 정보로 주어짐.

## 🔢 입력 조건

- 첫 줄: 정점 수 N (1 ≤ N ≤ 32,000), 간선 수 M (1 ≤ M ≤ 100,000)
- 다음 M줄: A B (A는 B보다 앞에 서야 함)

## 🎯 출력 조건

- 조건을 만족하는 학생들의 줄 서기 순서 출력
- 단, 가능한 여러 순서 중 하나 출력 가능

## 🧠 문제 핵심

- 조건 간 관계는 부분 순서(partial order) → 전체 순서를 구성하는 위상 정렬 필요
- 싸이클이 없는 방향 그래프(DAG) 구조여야 위상 정렬이 가능함

## 💡 관련 개념

- 위상 정렬 (Topological Sort)
- Directed Acyclic Graph (DAG)
- 진입 차수 (In-degree), 큐 (Queue)
