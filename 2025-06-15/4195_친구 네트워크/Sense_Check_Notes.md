# 📌 Sense Check Notes - BOJ 4195

## 1️⃣ 문자열 → 숫자 인덱스 변환이 왜 필요한가?

- Union-Find는 인덱스 기반 구조이기 때문에 문자열 입력을 숫자로 변환해야 처리 가능
- 문자열을 key로 쓰는 것도 가능하지만, **list[] 기반의 접근이 훨씬 빠르고 효율적**

## 2️⃣ name_to_id dict의 역할은?

- 처음 등장한 이름에 고유 숫자 ID를 부여하는 역할
- 이 ID를 기반으로 parent[], size[] 배열에서 해당 사람의 상태를 추적

## 3️⃣ size 배열은 어떤 역할을 하는가?

- 각 집합의 루트 노드에 **그 집합의 사람 수**를 저장
- union 시 루트를 병합하면서 size도 함께 누적
- 출력은 항상 `size[find(x)]`로 루트 기준으로 조회

## 4️⃣ 왜 append()를 쓰는가?

- Python list는 중간 인덱스 할당이 불가 → `parent[id] = id`는 오류
- append()를 사용해 ID가 늘어날 때마다 리스트 길이를 확장하며 index == value로 맞추는 방식이 안전하고 유연

## 5️⃣ 핵심 교훈

- 실전에서는 단순 연결 여부뿐 아니라 **상태 추적(크기 등)**이 함께 요구될 수 있음
- Union-Find + size + 문자열 인덱싱 조합은 매우 강력한 실전 알고리즘 도구
- Python에서는 dict ↔ list 구조 전환 시 성능과 안정성 모두 고려해야 함
