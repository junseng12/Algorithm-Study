# 💬 Reflection: BOJ 14725 개미굴

## 🧠 접근 과정 요약

- Node, Trie 클래스 정의
- insert 함수로 각 경로 문자열을 차례로 삽입
- DFS에서 sorted(children) 순회로 사전순 정렬 출력

## 🔄 시행착오 및 해결

- is_terminal로 종료조건 넣었다가 branch 누락 → 삭제
- dict 정렬할 때 .sort() 대신 sorted()로 수정
- root 출력 안하도록 dfs 시작 전 head에서 depth=0으로 설정

## ✅ 핵심 구현 포인트

- Node: key, children dict
- Trie: head Node, insert(path_list)
- DFS: sorted(children), print("--" \* depth + key)
- main 흐름: 입력 → insert → dfs 출력
