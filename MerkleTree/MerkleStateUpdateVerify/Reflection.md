# 🔍 Reflection: Merkle Tree 상태 업데이트 검증 시스템

## 💡 주요 구현 포인트

- `update_instructions.txt`를 통해 실시간 데이터 업데이트 시뮬레이션
- 각 변경 사항에 대해 Merkle Root 비교 및 Inclusion Proof 수행
- 로그 자동 생성으로 반복적 검증 시스템 구축

## 🤯 어려웠던 점

- 파일 경로 문제로 `FileNotFoundError` 발생
- 기존 `data` 배열과 업데이트 항목 간 관계 명확히 관리 필요
- Inclusion Proof 생성 시 잎 노드 복제 여부를 명확히 고려해야 함

## ✅ 개선 아이디어

- Root 변경 여부를 기준으로 **위변조 감지 시스템**으로 확장 가능
- 원본 상태 및 변경 이력 추적을 위한 시각화 툴 연계 가능

## 📌 오늘의 한 줄 회고

> "Merkle Tree는 데이터 변경을 ‘루트 하나’로 증명할 수 있는 강력한 구조였다."
