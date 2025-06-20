# 📌 Sense Check Notes - Custom Merkle Proof

## 1️⃣ 왜 XOR(1)로 sibling_index를 구하나?

- 인덱스가 짝수면 짝+1이 형제, 홀수면 홀-1이 형제
- XOR 1 연산은 이 두 경우를 한 줄로 처리 가능하게 해준다.

## 2️⃣ 해시 방향(dir)은 왜 필요할까?

- Merkle Proof 검증 시, 결합 순서에 따라 해시 결과가 달라진다.
- left/right 정보를 포함시켜야 정확한 경로를 계산 가능함

## 3️⃣ 왜 레벨 별 트리 구조를 유지하나?

- 각 레벨에서 해시를 병합하면서 최상위 루트로 향하는 구조이기 때문에,
- level 단위로 tree를 유지하면 증명 생성, 검증 모두 구조적으로 단순화된다.

## 4️⃣ 같은 데이터가 들어오면 YES 나와야 하는 이유는?

- 기존 루트는 바뀌지 않았으므로, 변경된 데이터가 실제로는 동일한 해시를 생성하면 루트도 같아짐
- 이 또한 정상적인 Proof 결과로 "YES" 출력
