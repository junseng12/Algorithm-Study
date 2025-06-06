# 📌 감각 메모

## 🔍 \[문제 이름]: `1182 - 부분수열의 합`

---

### 1. **DFS 함수에 어떤 변수를 매개변수로 넣을 것인가? (→ 상태 전달 요소)**

> **기준**: "탐색할 때마다 변하는 것 = 매개변수", "전체 탐색 동안 유지해야 할 값 = 전역 or 참조형"

| 변수          | 역할                       | 매개변수 여부 | 이유                                                       |
| ------------- | -------------------------- | ------------- | ---------------------------------------------------------- |
| `idx`         | 현재 인덱스 위치           | ✅ Yes        | 재귀마다 한 칸씩 전진하므로 현재 탐색 위치로서 필요        |
| `current_sum` | 지금까지 더한 부분합       | ✅ Yes        | 선택 여부에 따라 부분합이 달라지므로 탐색별 분기 기준이 됨 |
| `count`       | S를 만족하는 부분수열 개수 | ❌ No         | 전역 변수로 누적 관리. DFS 내부에서 갱신함                 |

---

### 2. **백트래킹 포인트는 어디인가? (→ 상태 복원 위치)**

> 이 문제에서는 **탐색 상태를 기록하지 않고**, 단순히 재귀 종료 이후 자연스럽게 복원되므로 별도 복구 필요 없음.

- 💡 선택/비선택 분기를 통해 자연스레 상태가 분기되므로 `visited`나 배열 복원 과정이 필요 없음
- 단, 그래프형 문제와 달리 \*\*명시적인 상태 복원이 없는 "조합형 DFS"\*\*임

---

### 3. **상태 변화의 최소 단위는 무엇인가? (→ 탐색 단계별 변화 단위)**

> 상태는 "지금까지 선택된 수들의 합"과 "지금 몇 번째 수를 볼 차례인지"에 의해 결정됨

| 요소          | 최소 변화 단위                  |
| ------------- | ------------------------------- |
| `idx`         | +1 (다음 숫자로 이동)           |
| `current_sum` | +numlist\[idx] 또는 그대로 유지 |

---

### 4. **탐색 대상은 누구인가? (→ 자식 노드 정의)**

> 현재 인덱스 `idx`에서 두 가지 선택을 함으로써 다음 탐색 대상(분기)을 정의

- `numlist[idx]`를 선택 → `current_sum += numlist[idx]`
- `numlist[idx]`를 선택하지 않음 → `current_sum` 유지

```python
dfs(idx + 1, current_sum + numlist[idx])  # 선택 O
dfs(idx + 1, current_sum)                # 선택 X
```

---

### 5. **기저 조건(Base case)은 어디인가?**

> **모든 원소에 대해 선택 여부를 결정한 후 (idx == N)** 종료

```python
if idx == N:
    if current_sum == S:
        count += 1
    return
```

- 💡 모든 수에 대해 선택이 끝났을 때만 부분합을 확인하고 count를 갱신

---

### 6. **그 외 이 문제에서 특이하게 고려할 요소는?**

| 요소                     | 설명                                                                    |
| ------------------------ | ----------------------------------------------------------------------- |
| ❗ 공집합 예외 처리 필요 | 문제에서 “크기가 양수인 부분수열” 명시 → `S == 0`일 때 공집합 제외 필요 |
| ❌ visited 필요 없음     | 중복 선택 X, index로 탐색이 정해져 있어 visited 불필요                  |
| ❌ graph 필요 없음       | 연결 구조 아님, 단순한 배열 탐색 구조                                   |

```python
# 공집합 제거 예시
if S == 0:
    count -= 1
```

---

## 🏁 최종 요약

| 항목               | 현재 문제에서의 적용                               |
| ------------------ | -------------------------------------------------- |
| ✅ 매개변수 선정   | `idx`, `current_sum` 만 사용                       |
| ✅ 백트래킹 포인트 | 없음 (재귀 분기로 자연스럽게 상태 구분됨)          |
| ✅ 상태 최소 단위  | 인덱스와 누적 합의 변화                            |
| ✅ 탐색 대상       | 각 원소를 **선택 / 비선택** 두 가지 분기           |
| ✅ 기저 조건       | `idx == N`일 때 부분합을 확인 후 종료              |
| ✅ 특이 요소       | `S == 0`일 때 공집합 예외 처리 필요 (`count -= 1`) |

---
