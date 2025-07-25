# 📌 Sense Check Notes - BOJ 1976

## 1️⃣ MST가 왜 필요 없는가?

- MST는 비용 최소화 목적
- 이번 문제는 비용 X → 연결 여부만 판단 → MST 구성 불필요
- **Union-Find로 연결 여부 판별만 하면 충분**

## 2️⃣ Union-Find를 어떻게 활용했는가?

- 인접행렬을 순회하면서 1인 경우 Union 처리
- 각 노드가 어느 집합에 속하는지 parent 관리
- 여행 계획 리스트 내 모든 도시의 parent가 동일하면 연결 가능 → YES 출력

## 3️⃣ 입력 처리 시 주의점

- 인접행렬이 1-based index로 주어짐 → 루프 설계 시 주의
- 자기 자신에 대해 Union 처리 필요 없음 (이미 같은 집합)

## 4️⃣ 여행 계획 검증 흐름

- 여행 계획 첫 도시의 parent 기록
- 나머지 모든 도시의 parent가 동일한지 확인
- 동일하지 않으면 NO, 모두 동일하면 YES 출력

## 5️⃣ 핵심 교훈

- **문제 요구 사항을 정확히 WHY 단계에서 분석** 후 올바른 알고리즘 선택이 중요
- Union-Find 사고 체계가 다양한 문제에 자연스럽게 적용됨을 경험
- MST → Union-Find → 순수 연결 여부 판별까지 사고 흐름 확장 경험 성공
