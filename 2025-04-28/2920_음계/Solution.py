# Problem: 2920 음계
# Date: 2024-04-28
# Language: Python 3

# 조건
# 다장조는 c d e f g a b C, 총 8개 음 존재 (c-> 1, d -> 2로 숫자로 바꾸어 표현)
# 연주한 순서 주어졌을 때 성질 판별

# 1부터 8까지 차례대로 연주한다면 ascending
# 8부터 1까지 차례대로 연주한다면 descending
# 둘 다 아니면 mixed

scale_list = list(map(int, input().split(' ')))

# 아이디어 : 
# 정렬한 값이 원래 배열과 같은 경우 => ascending 이거나 descending
# 정렬한 값이 원래 배열과 다른 경우 => mixed

ascending = sorted(scale_list)
descending = sorted(scale_list, reverse = True)

if (scale_list == ascending):
  print("ascending")
elif (scale_list == descending):
  print("descending")
else:
  print("mixed")