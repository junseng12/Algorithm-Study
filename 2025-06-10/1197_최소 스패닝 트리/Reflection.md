# 💬 Reflection: 최소 스패닝 트리 (BOJ 1197)

## 🧠 1. 접근 과정 요약

- MST 문제 유형을 처음 보고 "어떤 알고리즘을 써야 하는가?"부터 판단
- Kruskal / Prim 알고리즘이 있다는 것은 알고 있었음 → 시간복잡도 측면에서 Kruskal 선택
- MST 구성에서 "사이클 방지"가 중요한데, 이를 위해 Disjoint Set 사용 필요성 학습
- Kruskal 설계 흐름: **간선 정렬 → 간선 순차 처리 → Union-Find로 사이클 체크** 패턴으로 정리

## 🔄 2. 시행착오 및 사고 흐름

- Disjoint Set에서 왜 parent 리스트 초기화를 "자기 자신"으로 하는지 개념적으로 몰랐는데 이번 실습으로 정확히 이해
- Kruskal에서 visited 처리가 필요 없는 이유 학습 → 간선 중심 처리 + Union-Find가 이를 대체함
- edges.pop() 사용 시 정렬 방향 오류 발생 가능성을 실습 중 깨달음 → for 루프 사용 패턴이 더 안전함을 학습

## ✅ 3. 최종 구현 포인트

```python
edges.sort()
for w, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        total_weight += w
        edge_count += 1
        if edge_count == V - 1:
            break
```

## 🚩 4. 시간/공간 복잡도

- 시간 복잡도: O(E log E) + O(E α(N)) ≈ O(E log E)

- 공간 복잡도: O(V + E) (edges, parent 리스트 포함)
