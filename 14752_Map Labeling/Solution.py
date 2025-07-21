# Problem: 14752_Map Labeling
# Date: 2025-07-18
# Language: Python 3

# 조건
# 지도 레이블링: 지도 내 관심 있는 피처 옆에 텍스트 레이블 형태로 추가 정보를 표시하는 것
# 이 문제에서는 점 피처점 피처(마을, 도시 등)만 고려함

# 이 문제에서 레이블은 피처에서 멀리 떨어져 있어서 쌍으로 분리될 수 있습니다. 
# 그러나 각 피처는 연결선이라고 하는 직선을 포함하는 다각형을 통해 연관된 레이블에 연결되어야 함
# 분명히 연결선은 서로 교차해서는 안 됨

# 연결선은 두 종류만 존재 
# 1. 직선 연결선: 단일 수직선으로 구성
# 2. 굽은 연결선: 수직, 수평, 수직 선분인 세 개의 연결된 선분

# x축으로 간주되는 직선 L, 그 위에 포인트 피처에 해당하는 n개의 포인트 존재(n개의 포인트의 위치는 완전히 다름)
# 레이블: 평면에서 높이 1인 직사각형 영역
# 직사각형 레이블: 쌍으로 분리되어야 하지만 두 레이블의 경계는 접할 수 있음

# 각 포인트 p i: 너비가 w i 이고 높이가 1인 축과 평행한 직사각형 레이블 l i 와 연결됨
 
# 구부러진 커넥터의 개수가 최소화되도록 레이블의 위치를 찾는 프로그램 
# -> 직전 L 내 n 개의 포인트 제시되면.. 그것에 따라 직사각형 레이블 위치를 잘 조정하여.. 굽은 연결선이 최소가 되도록 설정해야 함

# 가정

## 입력 ##
# 첫 줄: 정수 n(1 ≤ n ≤ 10,000) (n은 점 피처에 해당하는 선 L에 있는 점의 개수)
# 다음 n개 줄의 "i번째 줄": n개 점 중 i 번째 점의 좌표 a i ( a i 는 정수이고 0 ≤ a i ≤ 10^8) (n개 점의 좌표는 엄격히 다름) ( i ≠ j 이면 a i ≠ a j )
# 그 다음 n개 줄의 "i 번째 줄": i 번째 점 의 연관된 레이블의 너비 w i (w i 는 정수이고, 1 ≤ w i ≤ 10^5 )

## 출력 ## 
# 모든 유효한 레이블 배치 중 최소 개수의 구부러진 커넥터 개수

# 아이디어 


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