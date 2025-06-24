# 💬 Reflection: Merkle Inclusion Proof 자동화 시스템

## 🧠 1. 접근 과정 요약

1. 파일 입력 → 리스트 `data` 생성 (`strip()` 필수).
2. `hash_fn` 으로 leaf 해시 계산 → `build_merkle_tree`.
3. 모든 인덱스에 대해 `generate_merkle_proof` 호출.
4. `verify_merkle_proof`로 루트와 비교 → 로그 기록.

## 🔄 2. 시행착오 및 사고 흐름

- Windows 기본 CP949 인코딩이 이모지(✅)를 지원하지 않아 `UnicodeEncodeError` 발생 → `encoding="utf-8"` 명시로 해결.
- Proof 생성 시 _홀수_ 리프에서 형제 해시가 누락돼 `elderberry` 검증 실패.  
  → `sibling_index ≥ len(level)`이면 **자기 해시 복제** 규칙 반영하여 해결.

## ✅ 3. 최종 구현 포인트

```python
if sibling_index < len(level):
    sibling_hash = level[sibling_index]
else:                # 홀수 리프 → 자기 복제
    sibling_hash = level[index]

proof.append({
    "hash": sibling_hash,
    "dir": "left" if index % 2 else "right"
})
```

## 🚩 4. 시간·공간 복잡도

- 트리 생성: O(N)

- Proof 생성·검증: O(log N) per leaf

- 전체: O(N log N) (모든 항목 자동 검증)
