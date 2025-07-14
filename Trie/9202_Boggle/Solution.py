# Problem: 9202_Boggle
# Date: 2025-07-14
# Language: Python 3

# 조건
# Boggle 게임 :  글자가 쓰여 있는 주사위로 이루어진 4×4 크기의 그리드에서 최대한 많은 단어를 찾는 게임
# Boggle에서 단어는 인접한 글자(가로, 세로, 대각선)를 이용해서 만들 수 있음

# 한 주사위는 단어에 한 번만 사용할 수 있음
# 단어는 게임 사전에 등재되어 있는 단어만 올바른 단어

# 점수 배점
# 1글자, 2글자로 이루어진 단어는 0점
# 3글자, 4글자는 1점, 5글자는 2점
# 6글자는 3점
# 7글자는 5점
# 8글자는 11점
# 점수 = 자신이 찾은 단어에 해당하는 점수의 총 합

# 단어 사전에 등재되어 있는 단어의 목록과 Boggle 게임 보드가 주어졌을 때, 얻을 수 있는 최대 점수, 가장 긴 단어, 찾은 단어의 수를 구하는 프로그램

# 가정

## 입력 ##
# 첫째 줄: 딘어 사전 내 단어의 수 w (1 < w < 300,000) 
# 다음 w개의 줄: 각 단어 (최대 8글자, 알파벳 대문자로만)
# 단어 다 주어지고 난 후, 빈 줄이 하나 주어짐

# 그 다음: Boggle 보드의 개수 b (1 < b < 30) (Boggle은 모두 알파벳 대문자로만, 각 Boggle 보드 당 4줄에 걸쳐 주어짐)
# 각 Boggle의 사이: 빈 줄이 하나 있음

## 출력 ## 
# 출력 양식 - (각각의 Boggle에 대해) 얻을 수 있는 최대 점수, 가장 긴 단어, 찾은 단어의 개수
# 한 Boggle에서 같은 단어를 여러 번 찾은 경우: 한 번만 찾은 것으로 셈
# 가장 긴 단어가 여러 개인 경우: 사전 순으로 앞서는 것 출력

# 아이디어 
# 단어 사전에 있는 단어들을 모조리 Trie 구조에 넣어놓음 (Trie 구조가 문자열 탐색이나 접두어 판별 효율적인 자료구조니까..)
# 

# ✅ Q1. 왜 Trie를 써야 할까?
# 힌트:
# 보글판에서 각 위치에서 시작하는 문자열 탐색 시,
# 매번 사전 리스트에서 모든 단어와 매칭 → O(N), 너무 느림
# Trie에 단어 등록 후, board를 DFS로 탐색하면서 prefix pruning!

# 👉 Q1. Trie로 prefix pruning을 하면 탐색 중 어디서 시간을 절약할 수 있을까?
# Trie 구조에 사전 내 단어들을 모조리 등록 후에 단어를 DFS로 탐색하면, 매번 리스트에서 탐색할 단어를 매칭할 때보다 효율적일 듯함.

# ✅ Q2. DFS 설계의 핵심은 무엇일까?
# 힌트:
# 현재 board[x][y]에서 시작
# 8방향 이동
# visited 배열로 경로 관리
# Trie에서 현재 prefix가 없으면 탐색 중단

# 👉 Q2. DFS 함수에 어떤 인자들을 넘겨야 할까? (예: 좌표, 현재 Trie node, 현재 단어, visited 등)
# 0 <= x <= 3, 0<= y <= 3 을 만족하는 x, y 값을 넘겨야 함. 그리고 이동 시에도 이 좌표 범위를 넘어가지 않도록 해야함
# DFS 처리하다 보니까, 현재 이어지고 있는 단어를 계속해서 인자로 넘겨줘야 하고, visited 배열도 [4][4]로 구성해서 해당 위치 단어 추가하면 True 처리하든 하여 다시 방문하지 못하게 관리 해야함 


# ✅ Q3. 점수 계산, 가장 긴 단어는 어떻게 관리할까?
# 힌트:
# 길이에 따라 점수 부여 표 존재
# 길이가 동일하면 사전순으로 비교해 더 앞선 단어 선택

# 👉 Q3. 탐색 중 발견한 단어들을 어떻게 기록/관리할까? (예: set, list, max_length, max_word 등)
# 한 단어 내 탐색 시에는 한 단어를 이어가며 dfs 에 전달하고, 최종 단어 완성 시 다른 set이나 list 자료 구조에 추가하여 기록함
# 점수 계산은 이 list 나 set 내 자료구조에 추가한 단어들의 길이를 고려하여 각 별 합산하여 최종 점수 계산함
# 말고 가장 긴 단어 관리 방법에 대해서는 생각 안남


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
        
# dfs 함수 설계 - 현재 (x, y) 위치에서, Trie를 따라가며 가능한 모든 단어를 탐색
def dfs(x, y, node, current_word, visited, found_words, board): 
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
       
    if (0<= x < 4 ) and (0 <= y < 4):
        if visited[x][y] :
            return

        char = board[x][y]
        
        if char not in node.children:
            return  # prefix pruning!
        
        next_node = node.children[char]
        next_word = current_word + char
        
        if next_node.is_terminal:
            found_words.add(next_word)
        
        visited[x][y] = True
        for dir in range(8):
            nx, ny = x + dx[dir], y + dy[dir]
            dfs(nx, ny, next_node, next_word, visited, found_words, board)
            
        visited[x][y] = False # backtracking
    else :
        return
    
# 빈 줄 스킵 함수
# wrapper 함수로 한 줄씩 소비하며 스킵
def read_nonblank():
    line = input()
    while line and not line.strip(): # 빈 줄인 동안 계속 읽기
        line = input()
    return line.rstrip('\n')
    
# 4×4 보드를 2차원 리스트로 읽어 반환하는 함수(다음 Board 입력받을 때도 항상 윗 빈 줄은 무시하므로 괜찮음)
def read_board():
    return [list(read_nonblank().strip()) for _ in range(4)]


score_table = [0, 0, 0, 1, 1, 2, 3, 5, 11]
def get_score(word):
    return score_table[min(len(word), 8)]

# 각 보드별 최종 결과 저장 자료구조
final_result = []

# 📘 입력 및 실행 루프
def main():
    # 단어 사전 내 단어의 수 입력받기
    w = int(input())    

    # 각 단어 입력받아 Trie 구조에 바로 넣기
    trie = Trie() 
    words = [input().strip() for _ in range(w)]
    for word in words:
        trie.insert(word)

    # 보드 개수 (빈 줄 스킵 → 바로 다음 블록)
    b = int(read_nonblank())
        
    for _ in range(b):
        # 4 X 4 board 2차원 배열 입력깂 받기
        board = read_board()                     # [['A','C','M','A'],...,]
        # 4 x 4 visited 2차원 배열 선언
        visited = [[False for row in range(4)] for col in range(4)]    
        
        # 찾은 단어 집합 선언(board에서 dfs 중 찾은 단어들 저장)
        found_words = set()
        
        # board 내 첫 출발점 잡기 - 모든 칸이 출발점이 될 수 있음
        for x in range(4):
            for y in range(4):
                char = board[x][y]
                #Trie 루트에서 시작 문자가 있는지 체크해서 없는 건 애초에 skip → pruning
                if char in trie.head.children :
                    dfs(x, y, trie.head, '', visited, found_words, board)
        
        max_score = 0
        # (각각의 Boggle에 대해) 얻을 수 있는 최대 점수 계산
        for word in found_words:
            max_score += get_score(word)
        
        longest_word = ''
        # 가장 긴 단어 찾기
        for word in found_words:
            if (len(longest_word) < len(word)):
                longest_word = word
            elif (len(longest_word) == len(word)) and word < longest_word:
                longest_word = word
        
        
        # 찾은 단어의 개수 세기
        num_found_words = len(found_words)
        
        final_result.append([max_score, longest_word, num_found_words])
    
    for score, word, count in final_result:
        print(f"{score} {word} {count}")
                
    
if __name__ == "__main__":
    
    
    main()