# Problem: [음계] ([2920])

- 링크: https://www.acmicpc.net/problem/2920

## 문제 요약

- 다장조는 c d e f g a b C, 총 8개 음 존재 (c-> 1, d -> 2로 숫자로 바꾸어 표현), 연주한 순서 주어졌을 때(숫자로 제공) 성질 판별

## 입력 조건

- [요약]
  1 2 3 4 5 6 7 8
  8 7 6 5 4 3 2 1
  8 1 7 2 6 3 5 4

## 출력 조건

- [요약]
  ascending
  descending
  mixed

## 생각할 포인트

- 아이디어 :
  정렬한 값이 원래 배열과 같은 경우 => ascending 이거나 descending
  정렬한 값이 원래 배열과 다른 경우 => mixed
