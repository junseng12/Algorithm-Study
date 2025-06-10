# ➕ Problem: 최소 스패닝 트리 (BOJ 1197)

- 링크: https://www.acmicpc.net/problem/1197

## 📌 문제 요약

- 주어진 무방향 그래프에서 MST(최소 스패닝 트리)를 구하고, MST의 가중치 총합을 출력
- MST는 모든 노드를 연결하면서 사이클이 없고, 간선 가중치 총합이 최소인 트리

## 🔢 입력 조건

- 정점 V (2 ≤ V ≤ 10,000)
- 간선 E (1 ≤ E ≤ 100,000)
- 이후 E줄 → u, v, w (정점 u-v 간의 가중치 w인 간선)

## 🎯 출력 조건

- MST의 가중치 총합 출력

## 🧠 문제 핵심

- E의 크기가 크므로 효율적 알고리즘 필요 (O(E log E) 수준)
- MST는 Kruskal 알고리즘(정렬 + Disjoint Set) 또는 Prim 알고리즘(우선순위 큐 기반)으로 구현 가능
- Kruskal 선택 시 사이클 체크를 위한 Disjoint Set 필요
- MST 완성 조건: **간선 V-1개 선택 완료**

## 💡 관련 개념

- 최소 스패닝 트리 (MST)
- Kruskal 알고리즘
- Disjoint Set (Union-Find)
- 그래프 정렬 처리
