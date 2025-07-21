# ➕ Problem: Merkle Inclusion Proof 자동화 시스템

## 📌 문제 요약

주어진 문자열 목록으로 이진 Merkle Tree를 만든다.  
각 항목(leaf)에 대해, 시스템이 생성한 Merkle Proof로 루트 해시와 일치하는지를 자동 검증해 “YES/NO”를 출력·기록한다.

## 🔢 입력 조건

- `data_sample.txt`
  - 첫째 줄부터 N 개의 문자열(길이 1 ~ 100 ASCII).
  - 공백·개행 제거 후 그대로 leaf 데이터로 사용.

## 🎯 출력 조건

- `ProofLog.md` 파일에 N 줄 기록
  - 포맷: `✅ {item} (Index {idx}): ✔️ YES` 또는 `❌ NO`

## 🧠 문제 핵심

- Merkle Tree 구성: 홀수 leaf → 자기 복제하여 짝수 맞춤.
- Proof 생성: 각 레벨에서 형제 해시와 방향(left/right) 저장.
- 검증: leaf hash → 루트 재귀적 결합 → 루트 일치 여부 판별.

## 💡 관련 개념

- SHA-256 해시
- Merkle Tree, Inclusion Proof
- 형제 인덱스: `sibling = index ^ 1`
- 홀수 리프 복제 처리
