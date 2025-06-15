# Problem: 4195_친구 네트워크
# Date: 2025-06-15
# Language: Python 3

# 조건
# 어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하라
# 친구 네트워크: 친구 관계만으로 이동할 수 있는 사이

# 가정
# 첫째 줄; 테스트 케이스의 개수
# 각 테스트 케이스의 첫째 줄: 친구 관계의 수 F(100,000을 넘지 않음)
# 다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어짐
# 친구 관계: 두 사용자의 아이디로 이루어짐
# 아이디 구성 - 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열

# 아이디어 : 



# 변수 구성
# Union-Find 로 풀이하는 문제임을 느꼈음. (각 서브 그룹 끼리 관계 집합을 점점 넓혀가면서 진행하는 느낌) 
# 각 친구 관계 집합에 다른 집합을 합집합하는 것인데.. 
# 합집합 할 때 루트가 같은 경우 그러니까, 같은 연결고리가 있는 경우에 집단 숫자를 늘릴 수 있음
# 두 사용자 A, B 놔두고... 뭔가 string으로 처리하니까 dict 자료구조 사용해서 빠르게 탐색도 할 수 있는 방안으로 진행하면 될 것 같음
# dict 자료구조가 리스트처럼 자료 추가하고 value 값 넣을 수 있는 듯하여.. union과 find 함수는 그대로 이용해도 되지 않을까 함



# # parent[x] >> parent.values(x) != x
# # parent.update({x: find(parent.values(x))})
# def find(x):
#     if parent.values(x) != x:
#         parent.update({x: find(parent.values(x))})  # 경로 압축
#     return parent.values(x)

# # parent[y_root] = x_root >> parent.update({y_root: x_root})
# def union(x, y):
#     x_root = find(x)
#     y_root = find(y)
#     if x_root != y_root:
#       parent.update({y_root: x_root})  # 또는 rank 기준으로 최적화 가능


import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

T = int(input())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]


# union() 함수에서 바로 네트워크 크기 반환하도록 설계 추천 ->> 성능 : O(N) -> O(1)
def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root  # 또는 rank 기준으로 최적화 가능
        size[x_root] += size[y_root]

def count_friend(x):
    return size[find(x)]


for i in range(T):
  F = int(input())
  parent = {}
  size = {}
  for _ in range(F):
    A, B = map(str, input().split())
    # A, B 모두 없을 수 있고, A만 없거나, B만 없거나,둘 다 있거나
    if (A not in parent) and (B not in parent):
      parent[A] = A
      size[A] = 1
      
      parent[B] = B
      size[B] = 1
      union(A, B)
    # 의미상 A가 B의 집합에 합병되는 느낌
    elif A not in parent:
      parent[A] = A
      size[A] = 1
      union(A, B)
    # 의미상 B가 A의 집합에 합병되는 느낌
    elif B not in parent:
      parent[B] = B
      size[B] = 1
      union(B, A)
    else:
      union(A, B)
    max_friend = count_friend(A)
    print(max_friend)
