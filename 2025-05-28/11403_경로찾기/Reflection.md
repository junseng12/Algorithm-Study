# 💬 Reflection: 경로 찾기 (BOJ 11403)

## 🧠 1. 접근 과정 요약

- 처음에는 DFS로 모든 정점 i에서 DFS를 수행하며 경로를 탐색
- 도달한 정점들을 기록해 출력 행렬 구성

## 🔄 2. 시행착오 및 사고 흐름

- 자기 자신으로 돌아오는 경로(i → i)를 DFS로 탐지하는 데 실패
- visited[i]를 DFS 시작 시 True로 설정하면서 사이클 경로를 놓침
  - 조건 분기에 따라 visited 처리하고, 특히 start == next 노드 처리로 사이클로 자신에게 돌아오는 케이스 처리함
  - 각 노드마다 방문 가능한 상황 처리를 위해... 매 dfs 처리 전 반복문마다, visited 배열을 새로 생성하여 각 dfs에서 방향 그래프 방문 상태를 초기화함
- i → i 경로는 자기 자신으로 되돌아오는 사이클 경로가 필요하다는 걸 인지함
- DFS만으로는 완전한 해결이 어려울 수 있음 → Floyd-Warshall 필요성 자각

## ✅ 3. 최종 구현 포인트

- 각 i에 대해 DFS 수행 후 visited 상태로 행렬 구성
- 자기 자신으로 되돌아오는 경우는 별도로 체크 필요
- 최종적으로 DFS보다는 플로이드 워셜 알고리즘이 더 적절하다는 인사이트 도출
