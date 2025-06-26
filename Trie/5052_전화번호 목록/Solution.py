# Problem: 5052_전화번호 목록
# Date: 2025-06-26
# Language: Python 3

# 조건
# 전화번호 목록 주어지고 일관성 유무 판단 프로그램
# 일관성을 유지: 한 번호가 다른 번호의 접두어인 경우가 없어야 함(한 번호가 다른 번호의 부분 집합이 되버리면 안됨)

# 가정
# 첫째 줄: 테스트 케이스의 개수 t (1 ≤ t ≤ 50)
# 각 테스트 케이스의 첫째 줄: 전화번호의 수 n (1 ≤ n ≤ 10000)
# ~다음 n개의 줄: 목록에 포함되어 있는 전화번호가 하나씩 주어짐

# 아이디어 
# 일단 입력된 전화번호 하나하나 기록함
# 기록한 전화번호 한 개 마다 반복문 돌며 다른 전화번호 내 포함 여부 검증 -> 딱봐도 뭔가 시간적으로 손해 볼 것 같음(기존 반복문 돌면서 요소 하나하나씩 대상 지정해서..)

# 📌 Q1. "전화번호 목록"에서 무엇이 Trie 구조에 적합한 이유일까?
# 그리고 어떤 상황에서 "BAD SET"이 되는 걸까?
# 전화번호의 prefix가 동일한 전화번호 유무를 판단하는 것에 
# Trie 구조가 해당하는 것과 유사한 문자열 검색에 대해서 빠르고 효율적이기 때문이다.
# data 가 있으면서, 동시에 children 이 같이 있다면 한 문자열이 다른 문자열의 부분집합이 될 수 있기 때문에 BAS SET이 된다고 판단했다.


# 📌 Q1. "전화번호 목록"에서 무엇이 Trie 구조에 적합한 이유일까?
# 그리고 어떤 상황에서 "BAD SET"이 되는 걸까?
# 전화번호의 prefix가 동일한 전화번호 유무를 판단하는 것에 
# Trie 구조가 해당하는 것과 유사한 문자열 검색에 대해서 빠르고 효율적이기 때문이다.
# data 가 있으면서, 동시에 children 이 같이 있다면 한 문자열이 다른 문자열의 부분집합이 될 수 있기 때문에 BAS SET이 된다고 판단했다.

import sys
input = sys.stdin.readline


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


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
            
            # Case 1: 탐색 중 종료된 문자열 있음
            if curr_node.data :
                return False
            
        # Case 2: 현재 문자열 삽입 완료 시점인데 자식이 존재함
        if curr_node.children:
            return False

        # 문자열이 끝난 지점의 노드의 data값에 해당 문자열을 표시
        curr_node.data = string
        return True


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
        

T = int(input())


for i in range(T):
    N = int(input())
    
    trie = Trie()
    
    result = True
    numbers = [input().strip() for _ in range(N)]
    for number in numbers:
        if trie.insert(number):
            continue
        else: 
            result = False
            break
    
    print("YES" if result else "NO")
 
            