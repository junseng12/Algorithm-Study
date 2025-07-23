# Problem: 7432_디스크 트리
# Date: 2025-07-24
# Language: Python 3

# 조건
# 디렉토리의 전체 경로가 모두 주어졌을 때, 디렉토리 구조를 구해 보기 좋게 출력하는 프로그램

# 가정
# 경로는 한 줄로 이루어져 있으며, 공백을 포함하지 않음
# 경로는 80글자를 넘지 않으며, 디렉토리는 역슬래시(\)로 구분된
# 각 디렉토리의 이름은 1~8글자이며, 알파벳 대문자, 숫자, 특수 문자로 이루어져 있음

## 입력 ##
# 첫째 줄: 중요한 디렉토리 전체 경로의 개수 N(1 ≤ N ≤ 500)
# 다음 N개 줄: 디렉토리 경로

## 출력 ## 
# 한 줄에 하나씩 디렉토리의 이름 출력
# 공백: 디렉토리 구조상에서 깊이 의미
# 각 서브 디렉토리는 사전 순으로 출력해야 하며, 부모 디렉토리에서 출력한 공백의 개수보다 1개 많게 공백 출력

# 아이디어 
# 한 입력 값에 대해 한꺼번에 들어온 \ 포함된 내용에 대해, 모두 리스트로 받아(/기준으로 나눠서) Insert 함수에 String으로 넘겨줌 => 바로 부모-자식 관계 유지하면 Trie 구성
# 직전 풀었던 문제와 너무 유사함

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.is_terminal = False


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    # 문자열 삽입
    def insert(self, string):
        curr_node = self.head

        # 삽입할 String 각각의 문자에 대해 자식Node를 만들며 내려간다.
        for char in string:
            # 자식Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            # 같음 문자가 있으면 노드를 따로 생성하지 않고, 해당 노드로 이동
            curr_node = curr_node.children[char]
        curr_node.is_terminal = True

    # 문자열이 존재하는지 탐색!
    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        # 탐색이 끝난 후에 해당 노드의 data값이 존재한다면
        # 문자가 포함되어있다는 뜻이다!
        if curr_node.data is not None:
            return True
        
# 이전 14725_개미굴 문제랑 너무 유사함
def dfs(node, depth):
        for char in sorted(node.children):
            print(" " * depth + char)
            child = node.children[char]
            dfs(child, depth+1)
        return

# 디렉터리 전체 경로의 개수
N = int(input())

# 각 정보 입력받아 Trie 구조에 바로 넣기
trie = Trie() 

# 각 입력받은 정보는 연결된 한 경로 내 정보이다. => 아예 데이터 넣을 떄 리스트로 받고, 이후 이어붙여가면서 진행
for _ in range(N):
    # 파이썬 기준, \ 을 기반으로 자르려면 \\ 써야 함
    directories = input().rstrip().split('\\')
    trie.insert(directories)


dfs(trie.head, 0)