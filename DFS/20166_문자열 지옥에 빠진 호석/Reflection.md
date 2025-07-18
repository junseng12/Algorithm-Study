# 💬 Reflection: BOJ 20166 문자열 지옥에 빠진 호석

## 🧠 접근 과정 요약

1. Query 입력 후 최대 query 길이 `MAX_LEN` 계산
2. DFS로 board의 모든 시작점에서 문자열 탐색
3. 탐색 과정에서 `count_map[s] += 1`로 결과 저장
4. Query마다 `count_map.get(query, 0)`으로 출력

## 🔄 시행착오 및 해결

- MAX_LEN 고정(5) 시 불필요한 조합 생성 → 동적 설정으로 최적화
- wrap-around 처리 제대로 안 했더니 일부 경로 누락 → 모듈로 연산으로 수정
- `count_map.get(query, 0)` 안 썼더니 KeyError 발생 → defensive coding 적용

## ✅ 핵심 구현 포인트

- `MAX_LEN = max(len(q) for q in queries)`
- DFS 시작 시 `depth=1, s=board[x][y]`
- `count_map[s] += 1` → 문자열 탐색 직후
- 이동은 `for dir` + modulo wrap-around
- Query output은 `count_map.get(query, 0)`

## ⏰ 시간/공간 복잡도

- 시간: \(O(N \times M \times 8^{L} + K)\), L = max query length (≤5)
- 공간: Map에 저장된 문자열 개수 = 보드 × 경로 수 (적정 수준)
