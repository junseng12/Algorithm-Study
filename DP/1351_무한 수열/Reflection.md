# 💬 Reflection: 무한 수열 (BOJ 1351)

## 🧠 1. 접근 과정 요약

- N값이 커서 배열 사용 불가 → dict로 메모이제이션.
- 재귀식 A(i)=A(i//P)+A(i//Q) 정의 후 중복 계산 방지.

## 🔄 2. 시행착오 및 사고 흐름

- 처음에는 DP 배열로도 가능할까 고민.
- 배열 대신 해시맵 사용 이유를 명확히 이해함.

## ✅ 3. 최종 구현 포인트

- Python dict memo={0:1} 준비
- 재귀 종료 조건: i=0에서 1 리턴
- sys.setrecursionlimit(10\*\*6) 추가

## 🚩 4. 시간/공간 복잡도

- 시간: O(log N) (중복 제거 덕분)
- 공간: O(number of unique i visited)
