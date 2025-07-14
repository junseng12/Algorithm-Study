import hashlib

# 간단한 SHA256 해시 함수 (Ethereum은 실제로 sha3 사용)
def hash_fn(data):
    return hashlib.sha256(data.encode()).hexdigest()

# MPT Node 클래스 정의
class Node:
    def __init__(self, node_type, path='', value=None):
        self.node_type = node_type      # 'branch', 'extension', 'leaf'
        self.path = path                # 공유 nibble 경로 (예: 'ca')
        self.value = value              # leaf: 값, extension: 자식 노드, branch: optional value
        self.children = {}              # branch 전용: { nibble: Node }
        self.hash = None                # node 해시 값

    # 노드 해시 계산 함수
    def compute_hash(self):
        if self.node_type == 'branch':
            # branch: 자식 노드들의 nibble:hash 문자열을 정렬해 연결
            data = ''.join(sorted(f"{k}:{v.hash}" for k, v in self.children.items()))
            if self.value:
                data += f"val:{self.value}"   # branch 자체 value가 있으면 포함
        elif self.node_type == 'extension':
            # extension: 공유 path + 자식 노드 hash
            data = f"path:{self.path},child:{self.value.hash}"
        else:  # leaf
            # leaf: path + 값
            data = f"path:{self.path},val:{self.value}"
        self.hash = hash_fn(data)
        return self.hash

# ----------------------- MPT 구성 예제 -----------------------

# 1️⃣ leaf node 생성
leaf_cat = Node('leaf', path='t', value='meow')   # 'cat' -> 'meow'
leaf_car = Node('leaf', path='r', value='drive') # 'car' -> 'drive'
leaf_dog = Node('leaf', path='og', value='bark') # 'dog' -> 'bark'

# 2️⃣ leaf node 해시 계산
leaf_cat.compute_hash()
leaf_car.compute_hash()
leaf_dog.compute_hash()

# 3️⃣ 'ca' prefix 공유 branch node 생성
branch_ca = Node('branch')
branch_ca.children['t'] = leaf_cat  # 'cat' 경로
branch_ca.children['r'] = leaf_car  # 'car' 경로
branch_ca.compute_hash()

# 4️⃣ 'ca' prefix 압축 extension node 생성
ext_ca = Node('extension', path='ca', value=branch_ca)
ext_ca.compute_hash()

# 5️⃣ root branch node 생성
root = Node('branch')
root.children['ca'] = ext_ca      # 'ca' extension node 를 root branch와 연결
root.children['d'] = leaf_dog     # 'dog' leaf를 root branch와 직접 연결
root.compute_hash()

# ----------------------- 출력 -----------------------

# 최종 root hash 출력
print(f"Root hash: {root.hash}")

# MPT 구조 출력
print("\n[MPT Structure]")
print(f" ROOT (branch) → ca (ext), d (leaf)")
print(f"  ca (extension) → branch (t:meow, r:drive)")
print(f"  d → og (leaf:bark)")
