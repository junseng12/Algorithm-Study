# Problem: 5052_전화번호 목록
# Date: 2025-07-07
# Language: Python 3

# 조건
# 어떤 모듈은 사전 내에서 가능한 다음 글자가 하나뿐이라면 그 글자를 버튼 입력 없이 자동으로 입력해줌
# 모듈 규칙:
# 모듈이 단어의 첫 번째 글자를 추론하지는 않는다. 즉, 사전의 모든 단어가 같은 알파벳으로 시작하더라도 반드시 첫 글자는 사용자가 버튼을 눌러 입력해야 한다.
# 길이가 1 이상인 문자열 c1c2...cn이 지금까지 입력되었을 때, 
# 사전 안의 모든 c1c2...cn으로 시작하는 단어가 c1c2...cnc로도 시작하는 글자 c가 존재한다면 모듈은 사용자의 버튼 입력 없이도 자동으로 c를 입력해 준다. 그렇지 않다면 사용자의 입력을 기다린다.

# 사전이 주어졌을 때, 이 모듈을 사용하면서 이와 같이 각 단어를 입력하기 위해 버튼을 눌러야 하는 횟수의 평균을 구하라

# 가정
# 각 테스트 케이스의 첫째 줄: 사전에 속한 단어의 개수 N (1 ≤ N ≤ 105)
# ~이어서 N개의 줄: 1~80글자인 영어 소문자로만 이루어진 단어 하나씩
# 이 단어들로 사전이 구성되어 있으며, 똑같은 단어는 두 번 주어지지 않음

# 입력으로 주어지는 단어의 길이 총합은 최대 10^6

# 출력 : 각 테스트 케이스마다 한 줄에 걸쳐 각 단어를 입력하기 위해 버튼을 눌러야 하는 횟수의 평균

# 아이디어 
# Trie 자료 구조를 통해서는 접두어 기반 문자열 탐색에 효율적으로 처리할 수 있음
# 따라서 Trie 구조 이용하여 각 단어를 입력할 때 Trie 자료 구조에 삽입시키고,
# 이후 계산할 때, 각 사전 내 단어를 하나하나씩 들고와서 사용자 입력 횟수를 카운트하고 이를 저장하여 종합적으로 평균내어 출력하면 되지 않을까?


# 📘 Q1. 문제 이해
# 총 N개의 단어가 주어졌을 때, 모든 단어를 자동완성 기능으로 입력할 때 평균적으로 몇 번의 키 입력이 필요한가?

# 단어들은 모두 Trie에 삽입됨

# 키 입력은 "다른 단어와 구분되는 시점"까지만 필요

# 즉, 노드의 자식이 여러 개이거나 해당 노드가 단어의 끝이라면 입력을 멈출 수 없음

# 자동완성은 현재 입력값에 대해서 자식이 여러 개가 아닌 경우에 처리될 수 있음. 그리고 해당 노드가 입력을 원했던 단어의 끝이라면 입력을 멈출 것이고 아니라면 추가 입력이 필요하다. 
# 따라서, 만약 모든 단어들이 첫 단어가 다 다르다고 한다면... 평균적으로 1번의 키 입력이 필요하다.


# ✏️ Q2. 개념 점검
# 다음 조건 중 자동완성을 위해 입력이 필요한 경우는?

# 현재 노드의 자식이 여러 개인 경우

# 현재 노드가 어떤 단어의 **끝 (is_terminal)**인 경우

# 현재 노드가 자식이 1개 뿐이고 is_terminal가 false인 경우

# 각 조건에 대해 입력이 필요한지 여부를 O/X로 판단해볼까?

# 자동완성을 위해서는 현재 입력값에 대해서 자식이 여러 개가 아닌 경우에 처리될 수 있다.
# 다만, 해당 현재 입력값에서 특정 단어가 끝이고, 이후 이어진 자식이 있는 경우라면.. 명확히 나누어 입력해줄 필요가 있음.
# 따라서, 현재 노드의 자식이 여러 개인 경우, 현재 노드가 자식이 1개 뿐이고 is_terminal가 false인 경우 자동완선을 위해 입력이 필요하다.



# 🧪 Q3. 입력 예제 시뮬레이션
# 예시 입력:
# 3
# hello
# hell
# heaven
# Trie를 구성했을 때 각 단어마다 몇 번의 키 입력이 필요한지, DFS 순회를 통해 추론해보자.

# "hello"는 어떤 지점까지 입력해야 하는가?
# h(e 자동입력)l (l 자동입력) 0 끝까지 입력해야 함, 총 3번
# "hell"은 언제 멈출 수 있는가?
# h(e 자동입력)l (l 자동입력) 총 2번
# "heaven"은 어느 경로에서 분기되는가?
# h(e 자동입력) a (V, e, n 자동입력) 총 2번
# a를 입력한 시점부터 l로 이어지는 다른 단어들과 분기되어 자동 완성 가능하다.



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
        
    

def need_input(node):
        return node.is_terminal or len(node.children) >= 2    


def dfs(node, depth):
        total = 0
        if node.is_terminal:
            total += depth

        for char in node.children:
            child = node.children[char]
            if need_input(node):
                total += dfs(child, depth + 1)
            else:
                total += dfs(child, depth)
        return total

# 📘 입력 및 실행 루프
def main():
    while True:
        try:
            N = int(sys.stdin.readline())
            trie = Trie()
            words = []
            for _ in range(N):
                word = sys.stdin.readline().strip()
                words.append(word)
                trie.insert(word)
            # ✅ DFS 호출 부분에서 루트의 자식부터 시작
            total_keystrokes = 0
            for child in trie.head.children.values():
                total_keystrokes += dfs(child, 1)
                
            average = total_keystrokes / N
            print(f"{average:.2f}")
        except:
            break

if __name__ == "__main__":
    main()
                