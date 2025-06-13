# 💬 Reflection: 여행 가자 (BOJ 1976)

## 🧠 1. 접근 과정 요약

- 문제 처음 보고 **MST 문제인지 잠깐 혼동** → 여행 경로가 주어지는 구조 → 단순 연결 여부 판단 문제임을 인식
- MST 필요 X → Union-Find만으로 연결 여부 판별 가능
- 인접행렬을 탐색하면서 Union-Find 초기화 및 Union 처리 진행

## 🔄 2. 시행착오 및 사고 흐름

- 인접행렬을 읽는 흐름에서 **자기 자신은 skip / 1인 경우에만 Union 수행** 로직 구성
- 여행 계획의 첫 도시의 대표 parent와 이후 도시들의 parent 비교 → parent가 모두 동일하면 YES
- 처음에 MST 구성 사고로 접근하려다 문제의 본질을 다시 WHY 단계에서 재확인하여 올바르게 사고 전환 성공

## ✅ 3. 최종 구현 포인트

```python
# 인접행렬에서 Union 처리(0-based)
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            # 노드는 1-Based 처리
            union(i+1, j+1)

# 여행 계획의 모든 도시 parent 비교
root = find(plan[0])
for city in plan[1:]:
    if find(city) != root:
        print("NO")
        break
else:
    print("YES")
```

## 🚩 4. 시간/공간 복잡도

- 시간 복잡도: O(N^2 α(N)) + O(M α(N))

- 공간 복잡도: O(N) (parent 리스트만 필요)
