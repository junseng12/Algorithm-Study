# 🧪 Merkle Tree 상태 업데이트 검증 시스템

## 🔢 입력 조건

- `original_data.txt`: 초기 데이터 N개 (각 줄마다 한 항목)
- `update_instructions.txt`: 한 줄마다 `"index new_value"` 형식의 업데이트 명령어
  - `index`: 0-based 인덱스
  - `new_value`: 새로운 값

## 🎯 출력 조건

- `UpdateLog.md`: 각 업데이트에 대해 다음 정보 출력
  - 업데이트 인덱스 및 변경 내용
  - 업데이트 전후 Merkle Root
  - Inclusion Proof 결과 (`YES` or `NO`)

## 🧠 문제 핵심

- Merkle Tree는 **불변성과 무결성 보장**에 적합한 구조
- 특정 노드를 수정할 경우, Merkle Root가 달라져야 정상
- 이를 통해 **데이터 위변조 탐지** 또는 **변경 검증** 수행 가능

## 💡 관련 개념

- SHA-256 기반 Merkle Tree
- Inclusion Proof 및 Root 비교
- 상태 변화 검증 시스템 설계
