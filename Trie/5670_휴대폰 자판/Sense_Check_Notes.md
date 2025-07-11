# 📌 Sense Check Notes - BOJ 5670

## 1️⃣ 왜 DFS가 적합한가?

- Trie에서 접두사 경로는 유일 → DFS로 전수조사 가능.
- BFS나 Dijkstra보다 간단하며, 분기만 잘 감지하면 효율적.

## 2️⃣ need_input()의 역할은?

- 자식 ≥2 (분기점) → 추가 입력 필요.
- is_terminal=True → 다른 단어와 구분 위해 입력 필요.

## 3️⃣ 예외/경계 조건은?

- 루트는 입력 전 상태.
- 루트 자식부터 DFS(depth=1) 시작해야 `"h"` 같은 한 글자 단어도 정확히 처리됨.

## 4️⃣ 더 발전시킬 여지

- Compressed Trie(압축 Trie)로 메모리 최적화.
- 한 번의 DFS에서 모든 쿼리 처리하는 메모이제이션 or DP 적용.
