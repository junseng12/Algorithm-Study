# 💬 Reflection: 도시 분할 계획 (BOJ 1647)

## 🧠 1. 접근 과정 요약

- 문제에서 "두 개의 마을로 분리"라는 표현을 보고 일반적인 MST 문제와 다른 **추가 전략 필요성** 인식
- MST 전체를 구성한 후 가장 비싼 간선 제거 전략을 WHY 단계에서 사고하여 적합성 판단
- Kruskal 알고리즘 기본 구조는 동일하게 적용 가능

## 🔄 2. 시행착오 및 사고 흐름

- 처음에 "언제 마을 분리를 적용할지" 고민 → 전체 MST 구성 완료 후 가장 비싼 간선 1개 제거가 최적이라는 구조 이해
- 구현 시 Kruskal 진행하면서 **가장 큰 간선 weight를 별도로 기록**하는 방식으로 설계
- MST 구성은 기존 1197/1922에서 익숙했던 패턴 그대로 적용 → 구조적 안정성 확보

## ✅ 3. 최종 구현 포인트

```python
edges.sort()
max_edge = 0
for w, u, v in edges:
    if find(u) != find(v):
        union(u, v)
        total_weight += w
        max_edge = max(max_edge, w)

print(total_weight - max_edge)
```

## 🚩 4. 시간/공간 복잡도

- 시간 복잡도: O(M log M) + O(M α(N)) ≈ O(M log M)

- 공간 복잡도: O(N + M) (간선 리스트 + parent 리스트)
