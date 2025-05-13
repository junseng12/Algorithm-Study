# Problem: 2798 블랙잭
# Date: 2024-04-30
# Language: Python 3

# 조건
# 카드의 합 <= 21 내에서 카드의 합을 최대한 크게 만들어야 함
# 각 카드에는 양의 정수 존재 (100,000이하)
# N(3 ≤ N ≤ 100) 장의 공개된 카드에서 M(10 ≤ M ≤ 300,000)을 외쳤을 때, N 장의 카드 중 3장을 골라, 카드합이 M을 넘지 않으면서 최대합인 조합을 찾아라

# 가정
# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어짐

# 아이디어 : 
# 목표 - A + B + C <= M 만족하는 A, B, C 값을 N개의 카드 내에서 선택하고 그 합을 제시하라..
# 수학적 공식 설계 관점으로 접근하였으나.. 쉽지 않음 (35분)
# Greedy 적인 관점에서 생각해보자 - 가능한 카드 중에 가장 큰 값 가진 카드 하나를 고르고 줄여나가는 것(아니라면 다음 큰 값 가진 카드로 넘어가면 되니까) > 반복문 처리(20분)

N, M = map(int, input().split())

Card = [None] * N;

Card = list(map(int, input().split()))

# Card 리스트 정렬
newCard = sorted(Card, reverse=True)
sumlist = []

# 큰 원소부터 꺼내어 M 값 이하의 최대합 조합 구성되는지 확인
for i in range(N):
  A = newCard[i]
  for j in range(i+1, N):
    B = newCard[j]
    for k in range(j+1, N):
      C = newCard[k]
      
      sum = A + B + C
      
      #구성되지 않는다면.. 다음 원소 기준으로 다시 최대합 조합 찾기
      if (sum > M):
        continue
      elif (sum <= M):
        sumlist.append(sum)


print(max(sumlist))