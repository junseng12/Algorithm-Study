# 💬 Reflection: BOJ 9202 Boggle

## 🧠 접근 과정 요약

- Trie로 사전 단어 등록 후, 보글판 각 좌표에서 DFS로 가능한 모든 단어 탐색.
- DFS 중에는 prefix pruning으로 불필요한 탐색 방지.
- found_words set에 찾은 단어 저장하여 중복 방지.

## 🔄 시행착오 및 사고 흐름

- DFS에서 current_word를 재귀 호출할 때 next_word로 갱신하지 않아 단어가 이어지지 않는 문제 발견.
- board를 전역 변수로 쓰지 않고, 명시적으로 인자로 넘겨야 함수 독립성 유지됨을 학습.
- is_terminal 플래그로 단어 완성 여부를 체크하는 로직의 중요성 체감.
- 점수 계산 및 최장 단어 찾기 로직에서 길이 동일 시 사전순 비교 조건 추가 필요.

## ✅ 최종 구현 포인트

- Trie insert → DFS with prefix pruning → visited 관리 + backtracking → 후처리 (점수/최장 단어/개수).
- set 사용으로 중복 방지.
- 점수 계산은 score_table로 매핑하여 처리.

## ⏰ 시간/공간 복잡도

- 시간 복잡도: O(4^L \* L) (L=단어 최대 길이, pruning 적용)
- 공간 복잡도: O(N \* L) (Trie, visited, found_words)
