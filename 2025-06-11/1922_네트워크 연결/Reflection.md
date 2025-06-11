# 💬 Reflection: 네트워크 연결 (BOJ 1922)

## 🧠 1. 접근 과정 요약

- 이전에 푼 1197 최소 스패닝 트리 문제와 구조적으로 거의 동일한 문제로 인식
- 따라서 MST 문제 → Kruskal 알고리즘 적용 판단
- 간선 정렬 → 순차 탐색 → Union-Find 사용으로 MST 구성

## 🔄 2. 시행착오 및 사고 흐름

- 문제 입력 형식과 1197이 거의 유사해서 **직접 구현하여 실행**
- 정답 코드에서 기존 MST 흐름을 그대로 적용했지만, 중간 중간 로직 재점검을 통해 구조 완전히 체득함
- MST의 종료 조건 (간선 N-1개)과 Union-Find 초기화 / 정렬 중요성 재확인

## ✅ 3. 최종 구현 포인트

```python
edges.sort()
for w, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        total_weight += w
        edge_count += 1
        if edge_count == N - 1:
            break
```

## 🚩 4. 시간/공간 복잡도

- 시간 복잡도: O(M log M) + O(M α(N)) ≈ O(M log M)

- 공간 복잡도: O(N + M) (간선 리스트 + parent 리스트)
