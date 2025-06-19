# 💬 Reflection: Merkle 루트 검증 시스템 (Custom Merkle Proof)

## 🧠 1. 접근 과정 요약

- 기존 Merkle Tree 개념을 구조적으로 이해한 뒤, 리프 → 루트 단계별 해시 처리 흐름 학습
- Proof에 필요한 형제 노드를 수집하는 방식(인덱스 XOR 1)이 핵심이었음
- 검증 시 왼쪽/오른쪽 방향에 따라 해시 순서를 바꾸는 것이 중요

## 🔄 2. 시행착오 및 사고 흐름

- 처음에는 트리 전체를 매번 재구성하는 방식으로 Proof 없이 단순 비교하려 했지만, 비효율적임
  - 비교할 데이터만 해시 처리
    -> 목표 인덱스를 기반으로 Merkle 증명 생성(기존 Tree에서 기존 데이터 기반 검증 생성)
    -> 해시 처리한 데이터를 기반으로 인덱스에 넣고 Merkle 증명 검증(목표 데이터가 Tree 내 해당 위치에 있었다면 검증 통과 / 아니면 검증 미통과)
    [구조적 이해 부족 확인]
- `sibling_index` 처리에서 off-by-one 에러 주의 (level 길이보다 클 수 없음)
- `proof`를 어떤 구조로 구성할지 고민했으나, 방향(dir) 정보를 포함한 딕셔너리로 처리해 가독성과 검증 정확성을 높임

## ✅ 3. 최종 구현 포인트

```python
sibling_index = index ^ 1
if sibling_index < len(level):
    proof.append({
        "hash": level[sibling_index],
        "dir": "left" if sibling_index < index else "right"
    })
```

## 🚩 4. 시간/공간 복잡도

- 트리 구성: O(N)

- Proof 생성: O(log N)

- 검증: O(log N)

- 총합: Q \* O(log N) (Q번 검증 수행)
