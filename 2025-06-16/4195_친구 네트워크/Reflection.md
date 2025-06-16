# 💬 Reflection: 친구 네트워크 (BOJ 4195)

## 🧠 1. 접근 과정 요약

- 입력이 문자열 기반이기 때문에 Union-Find를 직접 사용할 수 없음 → 문자열을 **숫자 인덱스**로 바꿔주는 `name_to_id` dict를 도입
- 사람 이름이 등장할 때마다 고유 ID를 부여하고, `parent[]`, `size[]`를 `append()`로 동적으로 확장
- 친구 연결 시 `union()`에서 두 집합을 병합하고 크기를 즉시 계산하여 출력하는 방식으로 설계

## 🔄 2. 시행착오 및 사고 흐름

- 처음에는 `dict` 기반으로 `parent[name]`, `size[name]` 형태로 접근하려 했지만, 배열 기반이 성능상 더 낫다는 점을 확인
  - 첫 아이디어 기반 구현 완료하였으나, 배열 기반 재학습 진행함
- `size[find(x)]` 구조로 실시간 크기 추적이 가능하다는 점을 실습을 통해 체득
- 중간에 `count_friend()`로 전체 parent를 순회하려는 시도를 했지만, 성능상 부적절하여 구조를 바꿈

## ✅ 3. 최종 구현 포인트

```python
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root
        size[x_root] += size[y_root]

# 초기화 예시
if name not in name_to_id:
    name_to_id[name] = id_counter
    parent.append(id_counter)
    size.append(1)
    id_counter += 1

# 연결 후 size 출력
union(id1, id2)
print(size[find(id1)])
```

## 🚩 4. 시간/공간 복잡도

- 시간 복잡도: O(α(N)) per union/find (거의 O(1))

- 공간 복잡도: O(N) for parent[], size[], and name_to_id dict
