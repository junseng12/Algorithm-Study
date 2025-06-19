# ➕ Problem: Merkle Inclusion (가칭 BOJ 20001)

- 커스텀 문제 : MerkleTree 이용 간이 문제
- 링크 없음

## 📌 문제 요약

- N개의 문자열 데이터가 주어집니다.
- 이들을 leaf로 하는 이진 Merkle Tree를 SHA256 으로 생성하고,
- 이후 Q개의 쿼리에 대해 “해당 문자열이 주어진 leaf index에 정말 포함되는지”를 증명하라

## 🔢 입력 조건

- 첫 줄: N, Q (1 ≤ N ≤ 2^20, 1 ≤ Q ≤ 10^5)
- 다음 N줄: `data_i` (길이 ≤ 100인 ASCII 문자열)
- 이후 Q줄: `i_k s_k`

  - `i_k`는 1-based leaf index (1 ≤ i_k ≤ N)
  - `s_k`는 길이 ≤ 100인 ASCII 문자열

## 🎯 출력 조건

- Q개의 줄에 각 쿼리에 대해

  - `YES` (해당 문자열이 그 인덱스의 leaf로 포함될 때)
  - `NO` (불일치할 때)

## 🧠 문제 핵심

- **Merkle Tree** 구조:

  - 각 `data_i`를 SHA256으로 해시 → 리프 해시 배열 생성
  - 레벨별로 짝이 없으면 자기 자신을 복제 → 부모 해시 계산
  - 루트 해시 하나로 전체 무결성 대표

- **Inclusion Proof**:

  - 특정 leaf 인덱스에서 루트까지 올라가며
  - 매 단계 **형제 노드의 해시 + 방향(left/right)** 저장
  - 저장된 proof로 루트 재계산 → 진위 확인

- **증명 과정**:

  1. `leaf_hash = SHA256(s_k)`
  2. `generate_proof(tree, index)`로 proof 리스트 수집
  3. `verify_proof(leaf_hash, proof, root_hash)`로 비교

## 💡 관련 개념

- **SHA256 해시 함수** (`hashlib.sha256`)
- **이진 Merkle Tree** 생성 및 순회
- **비트 연산** (XOR) 으로 형제 인덱스 계산
- **Proof 생성·검증 알고리즘**
- **무결성 검증**과 **데이터 포함 증명**
