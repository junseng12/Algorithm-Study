# ➕ Problem: 네트워크 연결 (BOJ 1922)

- 링크: https://www.acmicpc.net/problem/1922

## 📌 문제 요약

- N개의 컴퓨터를 모두 연결할 때 최소 비용을 계산
- 모든 컴퓨터를 연결하는 최소 비용 = **최소 스패닝 트리 (MST)** 문제

## 🔢 입력 조건

- 정점 수 N (1 ≤ N ≤ 1000)
- 간선 수 M (1 ≤ M ≤ 100,000)
- 이후 M줄: u, v, w (정점 u-v 간의 연결 비용 w)

## 🎯 출력 조건

- 모든 컴퓨터를 연결하는 최소 비용 출력

## 🧠 문제 핵심

- 전형적인 **무방향 MST 문제** (사이클 없는 최소 비용 연결)
- 노드 수는 작지만 간선 수가 크므로 정렬 기반 알고리즘(Kruskal)이 적합
- **Disjoint Set (Union-Find)** 자료구조 필요
- MST의 간선 수는 **N-1**

## 💡 관련 개념

- MST (최소 신장 트리)
- Kruskal 알고리즘
- Disjoint Set (Union-Find)
- Greedy, Graph Theory
