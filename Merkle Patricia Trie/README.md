# 📦 MPT Concept

## 📌 Modified Merkle Patricia Trie (MPT)란?

![alt text](<Merkle Partricia Tree_Instruction.png>)

Ethereum은 하나의 **state machine**이다.  
계정, 컨트랙트 등 모든 상태(state)는 key-value 쌍으로 표현되며, 이를 저장·관리하기 위해 **Modified Merkle Patricia Trie (MPT)** 라는 특수한 자료구조를 사용한다.

MPT는:

- Patricia Trie (prefix 압축 Trie) +
- Merkle Tree (해시 기반 무결성 구조) +
- Ethereum 특화 최적화

를 결합한 구조다.

---

## 🧩 MPT를 이루는 핵심 개념

### 1️⃣ Patricia Trie

- Trie (prefix tree): 공통 prefix를 공유하는 key들을 같은 경로로 합쳐 저장.
- Patricia Trie: 연속 단일 경로를 압축하는 Trie의 최적화 버전.
- 빠른 검색, 적은 메모리, 간단한 구현 → 라우터 같은 장비에서 routing table에 사용됨.

### 2️⃣ Merkle Tree

- Leaf node에 데이터 저장.
- 부모 노드는 자식들의 해시를 합쳐 다시 해시.
- root hash 하나로 전체 데이터셋의 무결성을 검증 가능.

### 3️⃣ MPT (Patricia Trie + Merkle Tree)

- Patricia Trie의 prefix 압축 + Merkle Tree의 해시 무결성.
- 각 노드: 자신의 내용과 자식 hash로부터 sha3 해시 생성.
- Ethereum은 levelDB(또는 rocksDB)에 `key=노드hash, value=노드내용`으로 저장.

---

## 🌍 MPT에서 표현되는 주소값들

Ethereum MPT에서 표현되는 key-value는:

- **계정 주소 (20바이트)** → balance, nonce, codeHash, storageRoot
- **스마트컨트랙트 storage key (32바이트)** → slot value

즉, 계정 레벨과 contract storage 레벨 모두 MPT로 관리되며,
prefix 경로는 nibble로 변환된 key, leaf node의 value는 상태 데이터(ex. ETH balance, storage slot 값)를 담는다.

---

## 🌳 MPT 노드 타입

![alt text](<Merkle Partricia Tree.png>)

| 노드 타입      | 구성                                     | 역할                                |
| -------------- | ---------------------------------------- | ----------------------------------- |
| Branch Node    | 16개 nibble slot (0~F) + value (총 17개) | prefix 분기 지점, 중간 노드         |
| Leaf Node      | [압축된 path, value]                     | 경로 끝에서 key-value 저장          |
| Extension Node | [압축된 path, 자식 hash]                 | 단일 자식만 가진 branch의 경로 압축 |

---

## 🔑 nibble 단위와 prefix의 이유

### ✅ nibble 단위 (4bit)

- 1 nibble = 4bit (0~F)
- Ethereum key (예: 20바이트 address) → 40 nibble
- 16분기(branch)로 나누면 Trie의 depth를 줄이고 lookup 속도를 높임.

### ✅ prefix의 역할

- leaf node와 extension node는 둘 다 `[path, 값/해시]` 형태.
- 구분 필요:
  - leaf:
    - 짝수 nibble → 0x20 prefix
    - 홀수 nibble → 0x3 prefix
  - extension:
    - 짝수 nibble → 0x00 prefix
    - 홀수 nibble → 0x1 prefix

### ✅ 왜 홀수/짝수 nibble에 prefix 길이가 다를까?

- 홀수 nibble: 남는 1 nibble → 1 nibble prefix 붙이면 byte 완성
- 짝수 nibble: 빈 nibble 없음 → 2 nibble prefix로 byte 완성
  → 항상 경로가 byte 단위로 저장되도록 정렬

---

## 📏 shared nibble(s)의 크기

- extension node의 shared nibble(s)는 prefix 압축 경로.
- 크기 제한 없음 → 여러 nibble(예: BEA)도 묶어 저장.
- 내부적으로는 nibble 수에 따라 byte 정렬을 위해 prefix로 패딩.

---

## ⚙️ extension node의 핵심 역할

- branch node의 자식이 단 하나만 있는 경우,
- 중간 branch node들을 경로(path) + 자식 hash로 압축.
- 메모리와 storage 효율을 높이고, 트리 depth를 줄임.

예:

```
0xBEA → 1000
```

- branch + extension → 굳이 안 쓰고,
- leaf node 하나로:

```
[ROOT]
 └ BEA (leaf node, value=1000)
```

즉, **leaf node 한 개만 연결되면 extension node 없이 바로 leaf로 압축**하는 게 메모리 효율적이다.

---

## 🏗️ 예제: 0xBEA → 1000, 0xBEE → 2000

```
[ROOT]
 └ BE (extension node, shared path="BE")
      └ [branch node]
          ├ A → leaf node (1000)
          └ E → leaf node (2000)
```

만약 0xBEA 하나뿐이라면:

```
[ROOT]
 └ BEA (leaf node, value=1000)
```

---

## 💥 MPT의 강점

✅ 빠른 검색·업데이트 (Patricia Trie)  
✅ 압축된 경로로 메모리·저장소 절약 (extension node)  
✅ root hash 하나로 전체 무결성 검증 (Merkle Tree)  
✅ Ethereum 대규모 상태 관리의 핵심 인프라

---

## 💻 MPT 간단 Python 구현

- MPT's Main IDEA (branch/extension/leaf + hash Management) implement Example

```python
import hashlib

def sha3(data):
    return hashlib.sha256(data.encode()).hexdigest()

class Node:
    def __init__(self, node_type, path='', value=None):
        self.node_type = node_type  # 'branch', 'extension', 'leaf'
        self.path = path  # shared nibble(s)
        self.value = value  # value or child hash
        self.children = {}  # for branch: {'a': Node, ...}
        self.hash = None

    def compute_hash(self):
        if self.node_type == 'branch':
            data = ''.join(sorted([c + child.hash for c, child in self.children.items()])) + (self.value or '')
        else:
            data = self.path + (self.value if self.node_type == 'leaf' else self.value.hash)
        self.hash = sha3(data)
        return self.hash

# 예제: 0xBEA → 1000, 0xBEE → 2000

# Leaf nodes
leaf_a = Node('leaf', path='A', value='1000')
leaf_e = Node('leaf', path='E', value='2000')
leaf_a.compute_hash()
leaf_e.compute_hash()

# Branch node under BE
branch = Node('branch')
branch.children['A'] = leaf_a
branch.children['E'] = leaf_e
branch.compute_hash()

# Extension node BE
ext = Node('extension', path='BE', value=branch)
ext.compute_hash()

# Root hash
print(f"Root hash: {ext.hash}")
```

### 🧩 이 코드에서 보여주는 핵심

✅ leaf node: [path, value]  
✅ extension node: [shared path, child]  
✅ branch node: 16 slots + optional value  
✅ 각 node의 hash: 자식 hash, path, value로 계산

### ⚡ 주의

- Ethereum 실제 MPT:
  - nibble encoding (0x00, 0x1, 0x20, 0x3)
  - sha3_256 (Keccak)
  - RLP encoding
  - levelDB, rocksDB에 key-value 저장

---

## 🌟 최종 정리

> MPT는 Ethereum의 state를  
> prefix Trie로 경로 압축하고,  
> Merkle 해시로 무결성을 보장하며,  
> 계정·storage 상태를 효율적으로 저장·검색하는  
> 블록체인 핵심 자료구조이다.

## Reference

- https://hamait.tistory.com/959
- https://medium.com/codechain-kr/modified-merkle-patricia-trie-ethereum%EC%9D%B4-%EC%83%81%ED%83%9C%EB%A5%BC-%EC%A0%80%EC%9E%A5%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95-e385f7d6bf84
